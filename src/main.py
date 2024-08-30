from speech_to_text import transcribe_audio
from text_to_speech import generate_speech
from conversation_manager import manage_conversations

def main():
    while True:
        user_input = transcribe_audio()
        if user_input.lower() == "exit":
            break

        response = manage_conversations(user_input)
        generate_speech(response)

if __name__ == "__main__":
    main()
