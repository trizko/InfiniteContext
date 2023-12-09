import os

from dotenv import load_dotenv

from llm import LLM

load_dotenv()

def main():
    print("Starting the conversation. Type 'quit' to exit.")
    chat_helper = LLM(api_key=os.getenv("OPENAI_API_KEY"), debug=True)

    while True:
        user_input = input("\n\033[92mYou:\033[0m ")
        if user_input.lower() == 'quit':
            break

        try:
            response = chat_helper.send_message(user_input)
            print("\n\033[95mAI:", response, "\033[0m")

        except ValueError as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()