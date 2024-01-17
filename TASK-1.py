import random

data = {
    "hi": "Hey there! I'm your friendly chatbot. How can I assist you?",
    "hello": "Hello! What can I do for you today?",
    "what is your name": "I'm just a chatbot, no name, but you can call me your virtual assistant.",
    "where are you from": "I exist in the digital realm, always ready to chat with you!",
    "how are you": "I'm just a program, but I'm here and ready to help you.",
    "do you have any hobbies or interests?": "My main interest is helping users like you! That's what I'm here for.",
    "what did you eat today?": "I don't eat, but I can help you discover amazing recipes and food-related information.",
    "what's your favorite color?": "I don't have preferences for colors; I'm here to assist you!",
    "do you enjoy listening to music?": "Unfortunately, I can't listen to music, but I'm happy to chat about it!",
    "bye": "Goodbye! Take care and feel free to return whenever you need assistance!",
    "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
    "who created you": "I was created by Krishna Kumar Manchala.",
    "what's the weather like today": "I'm sorry, I can't provide real-time weather information, but I can help you find a reliable weather website!",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "how old are you": "I don't have an age; I'm just a program designed to assist you.",
}

greetings = ["Hi!", "Hello!", "Hey there!", "Greetings!"]


def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't quite catch that. Could you please rephrase your sentence?"


print("Chatbot:", random.choice(greetings),
        "I'm a chatbot here to assist you!")

while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    if user_input == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    elif "capabilities" in user_input or "can you" in user_input:
        print("Chatbot: I can provide information, answer questions, and chat with you on various topics. Feel free to ask!")
    else:
        response = get_response(user_input)
        print("Chatbot:", response)
