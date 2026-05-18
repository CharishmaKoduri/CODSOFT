import random
import re



greetings = [
    "Hello! How can I help you today?",
    "Hi there! Nice to meet you.",
    "Hey! What would you like to know?"
]

goodbye_messages = [
    "Goodbye! Have a great day.",
    "See you again!",
    "Bye! Take care."
]

unknown_responses = [
    "Sorry, I did not understand that.",
    "Can you please rephrase your question?",
    "I am still learning. Try asking something else."
]


def chatbot_response(user_input):

    user_input = user_input.lower()


    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return random.choice(greetings)


    elif "your name" in user_input:
        return "I am a Rule-Based AI Chatbot created using Python."

   
    elif "artificial intelligence" in user_input or "ai" in user_input:
        return "Artificial Intelligence enables machines to learn and make decisions like humans."

 
    elif "python" in user_input:
        return "Python is a popular programming language used in AI, web development, and data science."

    elif "machine learning" in user_input:
        return "Machine Learning is a branch of AI where systems learn from data."

  
    elif "internship" in user_input:
        return "Internships help students gain practical experience and improve technical skills."

  
    elif "time" in user_input:
        return "Sorry, I cannot access real-time information."

 
    elif "study" in user_input or "education" in user_input:
        return "Consistent learning and practice are important for career growth."

  
    elif "thank you" in user_input or "thanks" in user_input:
        return "You are welcome!"

  
    elif user_input == "bye":
        return random.choice(goodbye_messages)

    
    else:
        return random.choice(unknown_responses)



print("\n========== AI CHATBOT ==========")
print("Type 'bye' to end the conversation.\n")

while True:

    user_message = input("You: ")

    response = chatbot_response(user_message)

    print("Bot:", response)

    if user_message.lower() == "bye":
        break
