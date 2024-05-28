import sys
import os
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../academia_tts')))
from academia_tts.tts import TTSProcessor


def main():
    if len(sys.argv) != 2:
        print("Usage: tts_pptx <path_to_pptx>")
        sys.exit(1)
    pptx_path = sys.argv[1]
    processor = TTSProcessor(pptx_path)
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"output_wav_{current_time}"
    presentation = processor.process(output_dir)
    output_pptx_path = f"output_{current_time}.pptx"
    presentation.save(output_pptx_path)
    print(f"The output presentation is saved as {output_pptx_path}")

if __name__ == "__main__":
    main()