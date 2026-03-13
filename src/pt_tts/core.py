import os
import asyncio
import ssl
import re

# Monkeypatch SSL to bypass certificate verification (needed for some proxies)
# This MUST happen before importing edge_tts or aiohttp to ensure they use the patched context.
if not hasattr(ssl, "_unverified_context_patched"):
    try:
        # Save the original method if needed later
        _original_create_default_context = ssl.create_default_context
        
        def _patched_create_default_context(*args, **kwargs):
            # Returns a context that does not verify certificates
            return ssl._create_unverified_context()
            
        ssl.create_default_context = _patched_create_default_context
        # Also patch the standard HTTPS context creation
        ssl._create_default_https_context = ssl._create_unverified_context
        ssl._unverified_context_patched = True
    except AttributeError:
        # Legacy Python or systems without _create_unverified_context
        pass

import edge_tts
import aiohttp
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from tqdm.asyncio import tqdm

class Gender(Enum):
    """Supported voice genders."""
    FEMALE = "female"
    MALE = "male"

@dataclass
class VoiceProfile:
    """Configuration for the TTS voice."""
    gender: Gender
    language: str = "pt-BR"
    
    @property
    def voice_name(self) -> str:
        """Returns the edge-tts voice identifier for the current profile."""
        if self.gender == Gender.FEMALE:
            return "pt-BR-FranciscaNeural"
        else:
            return "pt-BR-AntonioNeural"

@dataclass
class TTSRequest:
    """Encapsulates a text-to-speech conversion request."""
    input_file: Path
    output_file: Path
    voice: VoiceProfile

def validate_input_file(file_path: Path) -> None:
    """
    Validates that the input file exists and is readable.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
        PermissionError: If the file is not readable.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    if not file_path.is_file():
        raise IsADirectoryError(f"Path is not a file: {file_path}")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Permission denied reading file: {file_path}")

def get_output_path(input_path: Path) -> Path:
    """Generates the .mp3 output path based on the input filename."""
    return input_path.with_suffix(".mp3")

def _preprocess_text(text: str) -> str:
    """
    Preprocesses the text to ensure natural pauses for paragraphs and punctuation.
    """
    # Replace multiple newlines (paragraphs) with a short pause (ellipsis) and space
    # This helps the engine understand a clearer separation between ideas.
    text = re.sub(r'\n\s*\n', '\n\n... \n\n', text)
    return text.strip()

async def _do_conversion(text: str, voice_name: str, output_path: Path) -> None:
    """Internal async helper to perform the actual TTS conversion with a progress bar."""
    # Detecta proxy das variáveis de ambiente padrão do sistema
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY") or os.environ.get("https_proxy") or os.environ.get("http_proxy")
    
    # Se houver proxy, garantimos que ele tenha o esquema (http://)
    if proxy and not proxy.startswith("http"):
        proxy = f"http://{proxy}"

    if proxy:
        print(f"Using proxy: {proxy}")

    # Como WordBoundary não é garantido, vamos usar uma barra de progresso baseada em bytes
    # Ou uma barra indeterminada que mostra o progresso de "chunks" recebidos.
    # Para porcentagem, estimamos o total de caracteres como uma métrica aproximada.
    total_chars = len(text)
    
    communicate = edge_tts.Communicate(text, voice_name, proxy=proxy)
    
    # Usamos o total de caracteres como "total" aproximado
    pbar = tqdm(total=total_chars, unit="char", desc="Synthesizing", colour="green", leave=True)
    
    chars_processed = 0
    with open(output_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                # Atualizamos o progresso baseado no offset de caracteres se disponível
                # Se não, incrementamos proporcionalmente ao chunk de áudio ou frase.
                if "offset" in chunk and "text" in chunk:
                    # O edge-tts às vezes envia o offset em caracteres ou tempo.
                    # Vamos tentar uma abordagem mais simples: atualizar por frase/palavra
                    # Se for SentenceBoundary, podemos estimar o progresso pelo texto.
                    pass
                
                # Se for SentenceBoundary, vamos atualizar a barra proporcionalmente ao texto processado
                # mas o WordBoundary é melhor se vier. Como vimos que SentenceBoundary vem:
                pbar.update(len(text) // 5 if total_chars > 0 else 1)
            
            # Fallback: se recebermos áudio, garantimos que a barra se mova um pouco
            if chunk["type"] == "audio":
                 pbar.update(1)

    # Garante que a barra chegue a 100% no final
    pbar.n = total_chars
    pbar.refresh()
    pbar.close()

def convert_text_to_mp3(request: TTSRequest) -> None:
    """
    Converts the input file to an MP3 using the specified voice.
    """
    with open(request.input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if not text.strip():
        raise ValueError("Input file is empty or contains only whitespace.")

    processed_text = _preprocess_text(text)
    asyncio.run(_do_conversion(processed_text, request.voice.voice_name, request.output_file))
