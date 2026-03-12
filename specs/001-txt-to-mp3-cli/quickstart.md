# Quickstart: TXT to MP3 CLI

This guide provides usage examples and setup instructions for the `pt-tts` command-line tool.

## Setup

Ensure you have Python 3.10+ installed.

1. **Install Dependencies**:
   ```bash
   pip install edge-tts pytest
   ```

2. **Run Tool**:
   ```bash
   python main.py input.txt
   ```

## Usage Examples

### Basic Conversion
Convert a text file using the default voice.
```bash
python main.py documents/noticia.txt
# Generates documents/noticia.mp3
```

### Choose Female Voice
Use the `-f` flag to select a female voice.
```bash
python main.py -f news.txt
# Generates news.mp3 with a female voice
```

### Choose Male Voice
Use the `-m` flag to select a male voice.
```bash
python main.py -m news.txt
# Generates news.mp3 with a male voice
```

### Help
Show available commands and flags.
```bash
python main.py --help
```

## Troubleshooting

- **Error: Input file not found**: Ensure the path to your `.txt` file is correct and the file is readable.
- **Connection Error**: This tool requires an internet connection to use Microsoft Edge's high-quality neural voices.
- **MP3 not generated**: Check for write permissions in the target directory.
