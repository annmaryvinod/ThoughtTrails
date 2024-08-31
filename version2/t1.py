import streamlit as st
import openai
from gtts import gTTS
import speech_recognition as sr
import os
import time
import PyPDF2

# OpenAI API key setup (replace with your actual key)
openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # Use appropriate engine for open-source LLM
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    return "response.mp3"

def load_knowledge_base():
    knowledge_base_text = ""
    with open("./knowledge_base/conversation1.pdf", "rb" ) as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            knowledge_base_text += page.extract_text()
    return knowledge_base_text

def search_knowledge_base(knowledge_base, keyword):
    for doc in knowledge_base:
        if keyword in doc:
            return doc
    return None

def handle_conversation(user_input, knowledge_base):
    keywords = user_input.split()  # Simple keyword extraction
    for keyword in keywords:
        past_conversation = search_knowledge_base(knowledge_base, keyword)
        if past_conversation:
            return f"Do you remember the last time you talked about {keyword}? " \
                   f"{past_conversation}. Can you tell me more about it?"
    
    return "Tell me more about it."

def save_conversation(conversation, file_name="conversations/conversation_logs.txt"):
    with open(file_name, "a") as file:
        file.write(conversation + "\n")

st.title("Dementia Patient Journaling App")

st.write("Speak about your day, and I'll listen and save our conversation.")

if st.button("Start Conversation"):
    user_input = speech_to_text()
    st.write("You said:", user_input)

    knowledge_base = load_knowledge_base()
    response = handle_conversation(user_input, knowledge_base)
    st.write("AI:", response)
    
    # Convert AI response to speech and save as mp3
    audio_file = text_to_speech(response)
    
    # Play the audio within the Streamlit app
    st.audio(audio_file)
    
    # Save conversation
    save_conversation(f"User: {user_input}\nAI: {response}")
