from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

from rich import print
from rich.console import Console
from rich.text import Text
from rich_gradient.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

from pyfiglet import Figlet
from yaspin import yaspin
import textwrap
import inquirer
import os
import time

load_dotenv()
console = Console()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
# gemini_client = Gemini(api_key=os.getenv("GEMINI_API_KEY"))
# grok_client = Grok(api_key=os.getenv("GROK_API_KEY"))

def main_menu():
    questions = [
        inquirer.List(
            'action',
            message="Choose what to do:",
            choices=[
                'chat with ai',
                'write note',
            ],
        ),
    ]

    answer = inquirer.prompt(questions)
    choice = answer['action']
    return choice

def select_llm_model():
    choice = main_menu()
    if choice.strip() == 'chat with ai':
        # you could show a second menu here
        sub_q = [
            inquirer.List(
                'model',
                message="Choose model:",
                choices=['chatgpt', 'anthropic', 'grok']
            ),
        ]
        model = inquirer.prompt(sub_q)['model']
    else:
        model = None

    return model

def openai_chat_response(model: str, message: str):
    result = openai_client.responses.create(
        model="gpt-5",
        input=message,
        reasoning={"effort": "low"},
        text={"verbosity": "low"},
    )

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

    console.print("[bold violet]🌸✨💖 Hello, Star Coder, [magenta]You've Reached SARALOVE[/magenta] 🌸✨💖[/bold violet]")
    console.print("[bold yellow]💫⭐✨ Type freely the stars are listening ✨⭐💫[/bold yellow]\n")

    model = select_llm_model()
    console.print("[bold yellow]Type 'switch' to change LLM or 'menu' to return to main menu.[/bold yellow]\n")

    while True:
        console.print("[magenta]saralove >[/magenta] ", end="", highlight=False)
        command = input()

        if not command:
            console.print("\n[bold red]{-_-} Please enter a command {-_-}[/bold red]\n")
            continue

        if command == 'switch':
            select_llm_model()
            continue

        elif command == 'menu':
            main_menu()
            continue

        elif model == 'chatgpt':
            # Start spinner while waiting for response
            with yaspin(text="", color="magenta") as spinner:
                response = openai_chat_response(model, command)
                spinner.stop()

            print(Panel(f"\n{response}", border_style="magenta", title="ChatGPT 5")) # model’s reply
        
        elif model == 'anthropic':
            with yaspin(text="", color="magenta") as spinner:
                response = anthropic_chat_response(command)
                spinner.stop()
            
            print(Panel(f"{response}", border_style="red", title="Claude Sonnet 4.5")) # model’s reply

        elif model == 'ChatGPT 4o':
            print("\ngpt-4o is not supported yet\n")

if __name__ == '__main__':
    main()