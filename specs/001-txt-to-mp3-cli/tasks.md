# Tasks: TXT to MP3 CLI

**Input**: Design documents from `/specs/001-txt-to-mp3-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths assume single project structure at repository root as defined in plan.md.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/pt_tts/`, `tests/` directories
- [X] T002 [P] Create `requirements.txt` with `edge-tts` and `pytest`
- [X] T003 Initialize `src/pt_tts/__init__.py` and `tests/__init__.py`
- [X] T004 [P] Configure `.gitignore` for Python (`__pycache__`, `.pytest_cache`, `*.mp3`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and validation logic that MUST be complete before ANY user story

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Implement `TTSRequest` and `VoiceProfile` data models in `src/pt_tts/core.py`
- [X] T006 Implement input file validation (existence, readability) in `src/pt_tts/core.py`
- [X] T007 [P] Implement output path generation logic in `src/pt_tts/core.py`
- [X] T008 [P] Setup basic `argparse` skeleton in `src/pt_tts/cli.py`
- [X] T009 Create `main.py` entry point calling `cli.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Text-to-Audio Conversion (Priority: P1) 🎯 MVP

**Goal**: Convert a text file to an audio file using default Portuguese voice

**Independent Test**: Run `python main.py input.txt`. Verify `input.mp3` is created with spoken content.

### Implementation for User Story 1

- [X] T010 [P] [US1] Create unit test for default voice conversion in `tests/test_core.py`
- [X] T011 [US1] Implement `convert_text_to_mp3` using `edge-tts` in `src/pt_tts/core.py`
- [X] T012 [US1] Connect CLI to conversion logic in `src/pt_tts/cli.py`
- [X] T013 [P] [US1] Create integration test for basic CLI conversion in `tests/test_cli.py`

**Checkpoint**: MVP Ready - Basic conversion is fully functional.

---

## Phase 4: User Story 2 - Voice Gender Selection (Priority: P2)

**Goal**: Choose between a female and a male voice using `-f` and `-m` flags

**Independent Test**: Run `python main.py -f input.txt` and `python main.py -m input.txt`. Verify audio gender.

### Implementation for User Story 2

- [X] T014 [P] [US2] Create unit tests for gender-specific voice profiles in `tests/test_core.py`
- [X] T015 [US2] Update `VoiceProfile` to select correct `edge-tts` voice names (e.g., Francisca/Antonio) in `src/pt_tts/core.py`
- [X] T016 [US2] Add `-f` and `-m` flags to `argparse` in `src/pt_tts/cli.py`
- [X] T017 [US2] Update CLI to pass selected gender to core logic
- [X] T018 [P] [US2] Create integration tests for gender flags in `tests/test_cli.py`

**Checkpoint**: Gender selection is functional and integrated.

---

## Phase 5: User Story 3 - Error Handling for Missing Input (Priority: P3)

**Goal**: Clear error message when input file is missing

**Independent Test**: Run `python main.py non_existent.txt`. Verify error output.

### Implementation for User Story 3

- [X] T019 [US3] Implement robust error handling and user-friendly messages in `src/pt_tts/cli.py`
- [X] T020 [P] [US3] Create integration test for missing file error in `tests/test_cli.py`

**Checkpoint**: All user stories from specification are complete.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and verification

- [X] T021 [P] Implement edge case handling: Empty file behavior and special character validation in `src/pt_tts/core.py`
- [X] T022 [P] Add docstrings to all functions and classes
- [X] T023 Final run of `quickstart.md` validation
- [X] T024 [P] Final README.md update with usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

1. **Setup (Phase 1)** → **Foundational (Phase 2)**
2. **Foundational (Phase 2)** → **User Story 1 (Phase 3)**
3. **User Story 1 (Phase 3)** → **User Story 2 (Phase 4)** (Logical progression, though could be parallel if core handles gender)
4. **All Stories** → **Polish (Phase 6)**

### Parallel Opportunities

- T002, T004 (Setup)
- T007, T008 (Foundational)
- Unit tests (T010, T014) can be written in parallel with corresponding logic
- Polish tasks (T021, T022, T024)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Setup and Foundation.
2. Complete User Story 1.
3. Validate basic conversion.

### Incremental Delivery

1. Add Gender Selection (US2).
2. Add Error Handling (US3).
3. Final Polish.
