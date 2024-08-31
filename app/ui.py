# app/ui.py

import streamlit as st
from stt import speech_to_text
from tts import text_to_speech
from llm import generate_response

def App():
    st.title("AI LLM Journaling App for Dementia Patients")

    if st.button("Speak"):
        text = speech_to_text()
        if text:
            st.write(f"You said: {text}")

            # Generate response from LLM
            response = generate_response(text)
            st.write(f"LLM Response: {response}")

            # Convert LLM response to speech
            text_to_speech(response)
        else:
            st.write("Sorry, I didn't catch that.")

    if st.button("Save Conversation"):
        st.write("Conversation saved successfully!")
        # Implement saving logic here

if __name__ == "__main__":
    App()
