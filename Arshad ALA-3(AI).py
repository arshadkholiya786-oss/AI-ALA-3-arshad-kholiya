import math

def chatbot():
    print("ChatBot: Hello! I'm your assistant. Ask me anything (type 'bye' to quit).\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ("bye", "exit", "quit"):
            print("ChatBot: Goodbye! Stay curious. 👋")
            break

        # Basic math expression evaluation
        elif any(op in user_input for op in ['+', '-', '*', '/', '**']):
            try:
                result = eval(user_input)
                print(f"ChatBot: The answer is {result}")
            except Exception:
                print("ChatBot: Hmm... I couldn't calculate that. Make sure it's a valid expression.")

        # Square root
        elif "square root" in user_input:
            try:
                number = float(user_input.split()[-1])
                result = math.sqrt(number)
                print(f"ChatBot: The square root of {number} is {result}")
            except Exception:
                print("ChatBot: Please ask like 'square root of 16'.")

        # Logical thinking
        elif "riddle" in user_input or "logic" in user_input:
            print("ChatBot: Here's one! What has to be broken before you can use it?")
            answer = input("You: ").strip().lower()
            if "egg" in answer:
                print("ChatBot: Correct! 🥚")
            else:
                print("ChatBot: Nice try! The answer was 'an egg'.")

        # General knowledge
        elif "capital of france" in user_input:
            print("ChatBot: The capital of France is Paris.")
        elif "president of usa" in user_input:
            print("ChatBot: As of 2025, the President of the USA is Joe Biden.")
        elif "largest planet" in user_input:
            print("ChatBot: The largest planet in our solar system is Jupiter.")

        # Basic idea explanation
        elif "what is ai" in user_input:
            print("ChatBot: AI stands for Artificial Intelligence — machines that mimic human intelligence.")
        elif "what is python" in user_input:
            print("ChatBot: Python is a popular, easy-to-read programming language used for many types of software development.")
        elif "what is chatbot" in user_input:
            print("ChatBot: A chatbot is a software app that simulates conversation with human users.")
        elif "who is narendra modi" in user_input:
            print("ChatBot: Narendra Damodardas Modi (born 17 September 1950) is an Indian politician who has served as the prime minister of India since 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the member of parliament (MP) for Varanasi.")

        # Conversational responses
        elif user_input in ("hi", "hello", "hey"):
            print("ChatBot: Hello! How can I help you today?")
        elif user_input in ("india", "ind", "bharat"):
            print("ChatBot: India is a diverse, democratic republic composed of 28 states and 8 Union Territories, each with a unique culture, history, and identity, forming a tapestry of unity in its vast, multilingual, and multi-religious expanse.  ")
        elif user_input in ("us", "america", "united state"):
            print("ChatBot: The United Kingdom is a European island country composed of England, Scotland, Wales, and Northern Ireland, known for its rich history, cultural heritage, and constitutional monarchy. It features a blend of historic cities, ancient sites like Stonehenge, and scenic countryside.  ")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm working perfectly. 😄")
        elif "thank you" in user_input:
            print("ChatBot: You're welcome!")
        elif "who are you" in user_input:
            print("ChatBot: I'm a simple chatbot built with Python 3.10.")

        else:
            print("ChatBot: I’m not sure how to answer that. Try asking something else.")

# Run the chatbot
chatbot()
