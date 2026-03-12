import sys
import os

# Adiciona o diretório 'src' ao sys.path para permitir a importação do pacote 'pt_tts'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from pt_tts.cli import main

if __name__ == "__main__":
    sys.exit(main())
