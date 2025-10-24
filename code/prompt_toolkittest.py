from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'prompt': '#00ff00 bold',   # Green and bold for the prompt symbol
    'bottom-toolbar': '#888888 italic',
})

def get_input():
    user_input = prompt(
        [('class:prompt', '> ')],  # Prompt prefix
        style=style,
        bottom_toolbar="Press ? for shortcuts"
    )
    print(f"You typed: {user_input}")

get_input()
