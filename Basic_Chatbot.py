import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only the first time you run the script)
nltk.download('nps_chat')
nltk.download('punkt')

# Define a list of pairs (patterns and responses)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, how can I help you today?", "Hey there, how can I assist you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Janiita Khan. You can call me JKchatbot.",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm doing well! How about you?",]
    ],
    [
        r"what can you do?",
        ["I can have simple conversations with you and answer basic questions. How can I help you?",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day.", "Bye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase?",]
    ],
]

# Define a function to start the chatbot
def chatbot():
    print("Hi! I am a simple chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function to run the chatbot
if __name__ == "__main__":
    chatbot()
