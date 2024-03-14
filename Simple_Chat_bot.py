def simple_chatbot(user_input):
    
    user_input = user_input.lower()

   
    responses = {
        "hi": "Hello!",
        "how are you": "I'm fine, thank you!",
        "what's your name": "I'm a simple chatbot.",
        "bye": "Goodbye! Have a nice day!"
    }

   
    for key in responses:
        if key in user_input:
            return responses[key]

   
    return "I'm sorry, I don't understand that."

def main():
    print("Simple Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Simple Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)

if __name__ == "__main__":
    main()
