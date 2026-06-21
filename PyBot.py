def chatbot():
    print("====================================")
    print("      Welcome to Basic Chatbot")
    print("Type 'bye' to end the conversation.")
    print("====================================")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm doing great. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: My name is PyBot.")

        elif user == "who made you":
            print("Bot: I was created as part of a Python internship project.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions and have a basic conversation.")

        elif user == "what is python":
            print("Bot: Python is a popular programming language known for its simplicity.")

        elif user == "what is your favourite language":
            print("Bot: Definitely Python!")

        elif user == "what is today's date":
            print("Bot: Sorry, I can't tell the current date in this basic version.")

        elif user == "tell me a joke":
            print("Bot: Why do programmers prefer Python? Because it's easy to 'byte' into!")

        elif user == "thank you":
            print("Bot: You're welcome! Happy to help.")

        elif user == "thanks":
            print("Bot: Anytime!")

        elif user == "help":
            print("Bot: Try asking me:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- what can you do")
            print("- what is python")
            print("- tell me a joke")
            print("- thank you")
            print("- bye")

        elif user == "bye":
            print("Bot: Goodbye! Have a wonderful day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

chatbot()