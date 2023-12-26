from faster_whisper import WhisperModel
import os
import time

model_size = "large-v2"
model = WhisperModel(model_size, device="cuda", compute_type="int8")

def transcribe_audio():
    while True:
        try:
            audio_files = os.listdir("./output")
            if len(audio_files) < 2:
                continue
            audio_files.sort()
            audio_file = "./output/{0}".format(audio_files[0])

            segments, _ = model.transcribe(audio_file, beam_size=15)
            transcriptions = ""
            for segment in segments:
                transcriptions += segment.text
                output_file_name = "transcription/{0}.txt".format(time.strftime("%Y%m%d_%H%M"))
                with open(output_file_name, "a", encoding="utf-8") as f:
                    f.write(transcriptions)
            os.remove(audio_file)
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    transcribe_audio()