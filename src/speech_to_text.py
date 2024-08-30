from vosk import Model, KaldiRecognizer
import pyaudio
import json

def transcribe_audio():
    model_path = "src/model/vosk-model-small-en-us-0.15"  # Update path if different
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening...")
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result_json = recognizer.Result()
            result = json.loads(result_json)
            text = result.get('text', '')
            if text:
                print(f"Recognized: {text}")
                return text
            else:
                return "Sorry, I did not understand that."
        else:
            partial_result_json = recognizer.PartialResult()
            partial_result = json.loads(partial_result_json)
            print(f"Partial: {partial_result.get('partial', '')}")
