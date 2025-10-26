import ai_models as ai

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

console = Console()

def main_menu():
    questions = [
        inquirer.List(
            'action',
            message="Choose activity",
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
                message="Choose llm model",
                choices=['chatgpt', 'anthropic', 'gemini', 'grok']
            ),
        ]
        model = inquirer.prompt(sub_q)['model']
    else:
        model = None

    return model

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
            model = select_llm_model()
            continue

        elif command == 'menu':
            main_menu()
            continue

        elif model == 'chatgpt':
            # Start spinner while waiting for response
            with yaspin(text="", color="green") as spinner:
                response = ai.openai_chat_response(model, command)
                spinner.stop()

            print(Panel(f"\n{response}", border_style="green", title="ChatGPT 5")) # model’s reply
        
        elif model == 'anthropic':
            with yaspin(text="", color="red") as spinner:
                response = ai.anthropic_chat_response(command)
                spinner.stop()
            
            print(Panel(f"{response}", border_style="red", title="Claude Sonnet 4.5")) # model’s reply

        elif model == 'gemini':
            with yaspin(text="", color="blue") as spinner:
                response = ai.gemini_chat_response(command)
                spinner.stop()
            
            print(Panel(f"{response}", border_style="blue", title="Gemini 2.5 Flash")) # model’s reply

        elif model == 'grok':
            with yaspin(text="", color="grey") as spinner:
                response = ai.grok_chat_response(command)
                spinner.stop()
            
            print(Panel(f"{response}", border_style="grey", title="Grok 4")) # model’s reply

if __name__ == '__main__':
    main()