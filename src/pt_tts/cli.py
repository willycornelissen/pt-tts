import argparse
import sys
from pathlib import Path
from pt_tts.core import (
    Gender, VoiceProfile, TTSRequest, 
    validate_input_file, get_output_path, 
    convert_text_to_mp3
)

def parse_args():
    parser = argparse.ArgumentParser(description="Convert TXT files to MP3 using Portuguese TTS.")
    parser.add_argument("input_file", help="Path to the source .txt file")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--female", action="store_true", help="Use a female voice")
    group.add_argument("-m", "--male", action="store_true", help="Use a male voice")
    
    return parser.parse_args()

def main():
    args = parse_args()
    input_path = Path(args.input_file)
    
    try:
        validate_input_file(input_path)
        
        # Determine voice gender (default to Female as P1)
        gender = Gender.FEMALE
        if args.male:
            gender = Gender.MALE
        elif args.female:
            gender = Gender.FEMALE
            
        voice = VoiceProfile(gender=gender)
        output_path = get_output_path(input_path)
        
        request = TTSRequest(
            input_file=input_path,
            output_file=output_path,
            voice=voice
        )
        
        print(f"Synthesizing speech from {input_path} to {output_path}...")
        convert_text_to_mp3(request)
        print("Success!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
