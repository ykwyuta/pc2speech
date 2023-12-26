import soundcard as sc

import soundfile as sf
import time

def record():
    samplerate = 48000              # サンプリング周波数 [Hz]
    record_sec = 10                  # 録音する時間 [秒]

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=samplerate) as mic:
        while True:
            # デフォルトスピーカーから録音
            data = mic.record(numframes=samplerate*record_sec)
            output_file_name = "output/{0}.wav".format(time.strftime("%Y%m%d_%H%M%S"))
            sf.write(file=output_file_name, data=data, samplerate=samplerate)

if __name__ == "__main__":
    record()
