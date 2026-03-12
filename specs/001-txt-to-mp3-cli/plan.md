# Implementation Plan: TXT to MP3 CLI

**Branch**: `001-txt-to-mp3-cli` | **Date**: 2026-03-12 | **Spec**: [specs/001-txt-to-mp3-cli/spec.md]
**Input**: Feature specification from `/specs/001-txt-to-mp3-cli/spec.md`

## Summary

Build a Python-based CLI tool that converts text from a `.txt` file into an `.mp3` audio file using high-quality neural TTS voices (via `edge-tts`). The tool will support gender selection (male/female) and prioritize Portuguese linguistic accuracy.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: `edge-tts` (TTS), `argparse` (CLI)
**Storage**: Local file system (reads `.txt`, writes `.mp3`)
**Testing**: `pytest` for unit and integration tests
**Target Platform**: Linux, Windows, macOS (cross-platform)
**Project Type**: CLI tool
**Performance Goals**: Generate MP3 for 1KB text in under 5 seconds.
**Constraints**: Requires internet connection for `edge-tts` neural voices.
**Scale/Scope**: Small utility tool.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Open Source Only**: `edge-tts`, `argparse`, and Python are all Open Source. (Principle I)
- [x] **Portuguese Focus**: `edge-tts` provides high-quality Portuguese neural voices (pt-BR and pt-PT). (Principle II)
- [x] **Modular & Testable**: Core TTS logic will be in a library module, decoupled from CLI handling. (Principle III)
- [x] **Documentation as Code**: Spec, Plan, Research, and Tasks are all maintained as markdown in the repo. (Principle IV)
- [x] **Simple & Maintainable**: Minimal dependencies; straightforward CLI interface. (Principle V)

## Project Structure

### Documentation (this feature)

```text
specs/001-txt-to-mp3-cli/
├── plan.md              # This file
├── research.md          # Research on TTS libraries
├── data-model.md        # Feature entities
├── quickstart.md        # Usage examples
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
src/
├── pt_tts/
│   ├── __init__.py
│   ├── core.py          # Core TTS logic (library-first)
│   └── cli.py           # CLI interface (argparse)
├── tests/
│   ├── __init__.py
│   ├── test_core.py     # Unit tests for core logic
│   └── test_cli.py      # Integration tests for CLI
└── main.py              # Entry point
```

**Structure Decision**: Single project structure with a dedicated package `pt_tts` for modularity.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
