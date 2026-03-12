import pytest
from pathlib import Path
from pt_tts.core import VoiceProfile, Gender, TTSRequest, get_output_path, validate_input_file

def test_voice_profile_mapping():
    vp_female = VoiceProfile(gender=Gender.FEMALE)
    assert vp_female.voice_name == "pt-BR-FranciscaNeural"
    
    vp_male = VoiceProfile(gender=Gender.MALE)
    assert vp_male.voice_name == "pt-BR-AntonioNeural"

def test_output_path_generation():
    input_path = Path("test.txt")
    assert get_output_path(input_path) == Path("test.mp3")

def test_validate_input_file_non_existent(tmp_path):
    with pytest.raises(FileNotFoundError):
        validate_input_file(tmp_path / "non_existent.txt")

def test_validate_input_file_success(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello")
    # Should not raise any exception
    validate_input_file(test_file)
