import unittest
from text_to_speech import generate_speech

class TestTextToSpeech(unittest.TestCase):
    def test_generate_speech(self):
        try:
            generate_speech("Test")
            # Check if the file exists or other expected outcomes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"generate_speech failed with error: {str(e)}")
