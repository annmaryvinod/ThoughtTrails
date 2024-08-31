# app/llm.py

from transformers import pipeline

def generate_response(text):
    generator = pipeline('text-generation', model='gpt2')
    response = generator(text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
