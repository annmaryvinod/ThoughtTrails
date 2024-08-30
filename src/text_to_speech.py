from TTS.api import TTS

def generate_speech(text):
    tts = TTS("tts_models/en/ljspeech/glow-tts")
    tts.tts_to_file(text=text, file_path="response.wav")
    print("Generated speech saved to response.wav")
