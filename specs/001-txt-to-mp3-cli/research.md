# Research: Python TTS Libraries for Portuguese

## Topic: Best Open Source TTS Libraries for Python (Portuguese support)

### Candidates:
1. **gTTS (Google Text-to-Speech)**:
   - **Pros**: Easy to use, high-quality voices (Google Translate engine), excellent Portuguese support.
   - **Cons**: Requires internet connection (wraps an API), might have rate limits.
   - **License**: MIT (Open Source).
2. **pyttsx3**:
   - **Pros**: Offline support, works with native OS engines (SAPI5, NSSpeechSynthesizer, espeak).
   - **Cons**: Quality depends on the installed OS voices. Portuguese support depends on local installation.
   - **License**: MPC (Open Source).
3. **edge-tts**:
   - **Pros**: High-quality "Neural" voices from Microsoft Edge, supports Portuguese (pt-BR and pt-PT), no API key needed.
   - **Cons**: Requires internet connection.
   - **License**: MIT (Open Source).
4. **Coqui TTS**:
   - **Pros**: Advanced deep learning models, fully offline, very high quality.
   - **Cons**: Heavy dependencies, complex setup, models can be large.
   - **License**: Mozilla Public License 2.0 (Open Source).

### Decision:
We will use **`edge-tts`** for its superior "Neural" voice quality and ease of use, while keeping the dependency list manageable. Although it requires internet, it provides the best user experience for a CLI tool without the complexity of deep learning frameworks. We will also use **`argparse`** (stdlib) for CLI and **`pydub`** or a simple file write if `edge-tts` handles MP3 directly.

## Decision: Python Environment & Tools
- **Language**: Python 3.10+
- **CLI Framework**: `argparse` (Standard Library)
- **TTS Library**: `edge-tts`
- **Audio Handling**: `edge-tts` (generates MP3 directly)

## Rationale:
- `edge-tts` provides high-quality Portuguese voices (e.g., `pt-BR-FranciscaNeural`, `pt-BR-AntonioNeural`) which fulfills the requirement for female and male voices.
- Python is the requested language.
- All chosen libraries are Open Source.

## Alternatives Considered:
- `gTTS`: Quality is slightly lower than Edge Neural voices.
- `pyttsx3`: Quality is significantly lower as it uses old SAPI5/espeak voices.
- `Coqui TTS`: Overkill for a simple CLI tool.
