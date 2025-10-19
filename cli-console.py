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

def main():
    model = ask_llm_model()
    print(model)

if __name__ == '__main__':
    main()