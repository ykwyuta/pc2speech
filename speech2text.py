import gradio as gr
import time
import tempfile
from faster_whisper import WhisperModel
import os

model_size = "large-v2"
model = WhisperModel(model_size, device="cuda", compute_type="int8")

def transcribe_audio(audio_file):
    segments, _ = model.transcribe(audio_file, beam_size=15)
    transcriptions = ""
    for segment in segments:
        transcriptions += segment.text
        yield transcriptions

with gr.Blocks() as demo:
    input = gr.Audio(label="Select an audio file", format="mp3", sources=["upload"], type="filepath")
    output = gr.TextArea(label="Transcriptions")
    btn = gr.Button("Run")
    btn.click(fn=transcribe_audio, inputs=input, outputs=output)

demo.queue().launch(server_port=5000)
