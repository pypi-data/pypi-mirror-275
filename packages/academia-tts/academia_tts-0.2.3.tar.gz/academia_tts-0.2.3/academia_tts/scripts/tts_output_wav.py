import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../academia_tts')))
from academia_tts.tts import TTSProcessor

def main():
    if len(sys.argv) != 2:
        print("Usage: tts_output_wav <path_to_pptx>")
        sys.exit(1)
    pptx_path = sys.argv[1]
    processor = TTSProcessor(pptx_path)
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"output_wav_{current_time}"
    processor.process(output_dir)
    print(f"All audio files have been saved in the directory: {output_dir}")

if __name__ == "__main__":
    main()