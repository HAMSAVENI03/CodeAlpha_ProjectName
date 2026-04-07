def chatbot(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        print("Bot: Hi!")
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
    else:
        print("Bot: Sorry, I don't understand.")
print("Chatbot started (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    chatbot(user_input)
    if user_input.lower() == "bye":
        break