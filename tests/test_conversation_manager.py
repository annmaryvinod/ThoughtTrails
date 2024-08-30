import unittest
from conversation_manager import manage_conversations

class TestConversationManager(unittest.TestCase):
    def test_manage_conversations(self):
        response = manage_conversations("Test input")
        self.assertIn("You said: Test input", response)
