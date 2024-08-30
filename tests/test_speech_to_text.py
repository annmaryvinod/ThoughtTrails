import unittest
from speech_to_text import transcribe_audio

class TestSpeechToText(unittest.TestCase):
    def test_transcribe_audio(self):
        result = transcribe_audio()
        self.assertIsInstance(result, str)
        # Additional assertions based on expected behavior
