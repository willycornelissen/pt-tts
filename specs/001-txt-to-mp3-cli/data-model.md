# Data Model: TXT to MP3 CLI

## Entities

### TTSRequest
Represents a single text-to-speech conversion request.

- **input_file**: Path to the source `.txt` file. (String/Path, Required)
- **output_file**: Path where the resulting `.mp3` will be saved. (String/Path, Required)
- **voice**: The selected voice profile (Gender/Language). (Object, Required)

### VoiceProfile
Defines the characteristics of the synthesized voice.

- **gender**: Selection of 'female' or 'male'. (Enum, Required)
- **language**: Target language code (Default: 'pt-BR'). (String, Required)
- **voice_name**: The specific `edge-tts` voice identifier (e.g., `pt-BR-FranciscaNeural`). (String, Internal)

## Validation Rules
- **Input File**: MUST exist and be readable. Extension SHOULD be `.txt`.
- **Output File**: Base directory MUST be writable.
- **Gender**: MUST be either 'female' or 'male'. Defaults to a chosen system default if unspecified.
