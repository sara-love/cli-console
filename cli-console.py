from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

from rich import print
from rich.console import Console
from rich.text import Text
from rich_gradient.text import Text
from rich.prompt import Prompt

from pyfiglet import Figlet
from yaspin import yaspin
import textwrap
import inquirer
import os

load_dotenv()
console = Console()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def select_llm_model():
    questions = [
        inquirer.List(
            'LLM-model',
            message="Pick a model",
            choices=['openai', 'anthropic'],
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers['LLM-model']

def openai_chat_response(model: str, message: str):
    result = openai_client.responses.create(
        model="gpt-5",
        input=message,
        reasoning={"effort": "low"},
        text={"verbosity": "low"},
    )
    # Add newline before printing
    print("\n" + result.output_text)

    return result.output_text

def anthropic_chat_response(query: str):
    result = anthropic_client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": query}
        ],
    )

    return result.content[0].text

def main():
    f = Figlet(font='ansi_shadow')
    banner = f.renderText("SARALOVE")
    lines = banner.splitlines()

    console.print("\n")
    for line in lines:
        text = Text(line, colors=["#E56AB3", "#EF87B5", "#F9A3CB", "#FCBCD7"])
        console.print(text)

    print("[bold yellow]Type 'switch' anytime to change the model.[/bold yellow]\n")

    model = select_llm_model()
    print(f"[bold blue]You chose: {model}[/bold blue]")

    while True:
        command = Prompt.ask("\n[bold green]ME > [/bold green]") # displays the prompt without a newline

        if command == 'switch':
            model = select_llm_model()
            print(f"[bold blue]You chose: {model}[/bold blue]")
            continue

        if model == 'openai':
            # Start spinner while waiting for response
            with yaspin(text="", color="magenta") as spinner:
                response = openai_chat_response(model, command)
            
            wrapped_response = textwrap.fill(response, width=120)
            print(f"\n[bold magenta]{model}[/bold magenta]> {wrapped_response}") # model’s reply
        
        elif model == 'anthropic':
            with yaspin(text="", color="magenta") as spinner:
                response = anthropic_chat_response(command)
            
            wrapped_response = textwrap.fill(response, width=120)
            print(f"\n[bold magenta]{model}[/bold magenta]> {wrapped_response}") # model’s reply

        elif model == 'ChatGPT 4o':
            print("\ngpt-4o is not supported yet\n")

if __name__ == '__main__':
    main()