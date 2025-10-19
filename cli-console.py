from openai import OpenAI
from dotenv import load_dotenv
import inquirer
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm_model():
    questions = [
        inquirer.List(
            'LLM-model',
            message="Pick a model",
            choices=['gpt-5', 'gpt-4o'],
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers['LLM-model']

def openai_chat_response(model: str, message: str):
    result = client.responses.create(
        model=model,
        input=message,
        reasoning={"effort": "low"},
        text={"verbosity": "low"},
    )
    return result.output_text

def main():
    model = ask_llm_model()
    print(f"You chose: {model}")

    while True:
        command = input(":")

        if command == 'switch':
            model = ask_llm_model()
            print(f"You chose: {model}")
        else:
            response = openai_chat_response(model, command)
            print(response)

if __name__ == '__main__':
    main()