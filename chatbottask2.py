import nltk
import random
import re
from nltk.chat.util import Chat, reflections


nltk.download('punkt')


bot_responses = [
    (r"hi|hello", ["Hello!", "Hi there! How can I assist you today?"]),
    (r"how are you", ["I'm an AI, so I don't have feelings, but I'm here to help you."]),
    (r"what is your name", ["you can call me MUX."]),
    (r"bye", ["Goodbye! If you have more questions, feel free to ask."]),
    (r"what can you do", ["I can provide information, answer questions, and engage in meaningful conversations."]),
    (r"your age", ["I don't have an age. I am a program designed to assist you effectively."]),
    (r"thank you", ["You're welcome! If you need further assistance, feel free to ask."]),
    (r"how can I contact support", ["For support, please contact our customer service at support@example.com."]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]),
    (r"help", ["I'm here to help! Please specify your question or concern, and I'll do my best to assist you."]),
    (r"favorite color", ["I don't have a favorite color. I'm here to assist you with any questions you may have."]),
    (r"tell me about yourself", ["I am a sophisticated chatbot designed to provide assistance and information."]),
    (r"how does your algorithm work", ["My algorithm is based on natural language processing techniques to understand and respond to user input."]),
    (r"what's the meaning of life", ["The meaning of life is subjective and varies for each individual. What's meaningful to you?"]),
    (r"recommend a book", ["I recommend 'Sapiens: A Brief History of Humankind' by Yuval Noah Harari."]),
    (r"weather today", ["I'm sorry, I don't have real-time information. You can check a reliable weather website for the current weather."]),
    (r"tell me a fun fact", ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]),
    (r"learn programming", ["There are various online platforms like Codecademy, Udacity, and Coursera that offer programming courses for beginners."]),
    (r"news today", ["I recommend checking reputable news websites or apps for the latest news updates."]),
    (r"tell me a story", ["Once upon a time in a distant land, there was a curious adventurer who embarked on a journey to discover the secrets of a hidden treasure..."]),
    (r"(.*)", ["I'm sorry, I didn't quite catch that. Could you please rephrase your statement or question?"]),
]




class ProfessionalChatBot(Chat):
    def __init__(self, pairs, reflections={}):
        super().__init__(pairs, reflections)
    
    def respond(self, input_message):
        response = None
        for pattern, responses in self._pairs:
            if re.match(pattern, input_message.lower()):
                response = random.choice(responses)
                break
        return response if response else random.choice(self._reflections["default"])





professional_bot = ProfessionalChatBot(bot_responses, reflections)

print("Bot: Hello! I'm a chatbot named 'mux' here to assist you. How can I help you today?")

while True:
    user_input = input("You: ")
    response = professional_bot.respond(user_input)
    print("Bot:", response)
    
    if user_input.lower() == 'bye':
        print("Bot: Goodbye! If you have more questions in the future, feel free to reach out.")
        break
