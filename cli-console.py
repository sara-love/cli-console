import textwrap
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from yaspin import yaspin
import inquirer
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm_model():
    questions = [
        inquirer.List(
            'LLM-model',
            message="Pick a model",
            choices=['ChatGPT 5', 'ChatGPT 4o'],
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers['LLM-model']

def openai_chat_response(model: str, message: str):
    result = client.responses.create(
        model="gpt-5",
        input=message,
        reasoning={"effort": "low"},
        text={"verbosity": "low"},
    )
    return result.output_text

def main():
    model = ask_llm_model()
    print(f"[bold blue]You chose: {model}[/bold blue]")

    while True:
        print("\n[bold green]ME > [/bold green]", end="") # displays the prompt without a newline
        command = input()  # read user input

        if command == 'switch':
            model = ask_llm_model()
            print(f"[bold blue]You chose: {model}[/bold blue]")
            continue

        if model == 'ChatGPT 5':

            # Start spinner while waiting for response
            with yaspin(text="", color="magenta") as spinner:
                response = openai_chat_response(model, command)
            
            wrapped_response = textwrap.fill(response, width=120)
            print(f"\n[bold magenta]{model}[/bold magenta]> {wrapped_response}") # model’s reply
        
        elif model == 'ChatGPT 4o':
            print("\ngpt-4o is not supported yet\n")

if __name__ == '__main__':
    main()