# pt-tts Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-12

## Active Technologies

- Python 3.10+ + `edge-tts` (TTS), `argparse` (CLI) (001-txt-to-mp3-cli)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] .venv/bin/pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] .venv/bin/ruff check .

## Code Style

Python 3.10+: Follow standard conventions

## Recent Changes

- 001-txt-to-mp3-cli: Added Python 3.10+ + `edge-tts` (TTS), `argparse` (CLI)
- 001-txt-to-mp3-cli: Fixed SSL certificate verification error (`SSLCertVerificationError`) for corporate proxies by monkey-patching `ssl.create_default_context`.
- 001-txt-to-mp3-cli: Added a progress bar using `tqdm` and improved natural pauses between paragraphs by pre-processing text with elipses (`...`).

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
