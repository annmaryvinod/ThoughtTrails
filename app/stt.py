# app/stt.py
import sys
print("Python path:", sys.path)

import vosk
import sounddevice as sd
import queue
import json

# Path to the Vosk model
model_path = "vosk-model/vosk-model-small-en-us-0.15"

# Initialize Vosk model
model = vosk.Model(model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def speech_to_text():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Listening...")

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                text = json.loads(result)["text"]
                print(f"Recognized Text: {text}")
                return text
            # If you need to handle other cases, you can add more conditions here
