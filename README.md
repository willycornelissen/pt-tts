# pt-tts: TXT to MP3 CLI

A simple Command Line Interface (CLI) to convert Portuguese `.txt` files into high-quality `.mp3` audio files using neural TTS voices.

## Features

- Converts UTF-8 text files to MP3.
- High-quality Portuguese neural voices (Male and Female).
- Automatic output filename generation.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Basic conversion (default voice):
```bash
python main.py input.txt
```

Select female voice:
```bash
python main.py -f input.txt
```

Select male voice:
```bash
python main.py -m input.txt
```

## Development

Run tests:
```bash
pytest
```
