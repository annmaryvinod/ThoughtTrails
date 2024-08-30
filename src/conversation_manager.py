from datetime import datetime

def manage_conversations(user_input):
    response = "You said: " + user_input  # Simple echo response; replace with more complex logic
    save_conversation(user_input, response)
    return response

def save_conversation(user_input, response):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/conversations/conversation_{date_str}.txt"
    with open(filename, 'a') as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Response: {response}\n\n")
