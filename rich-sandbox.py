from time import sleep

from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console = Console()

with console.screen(style="bold white on red") as screen:
    for count in range(5, 0, -1):
        text = Align.center(
            Text.from_markup(f"[blink]Don't Panic![/blink]\n{count}", justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text))
        sleep(1)

# 🎨 Basic Named Colors
# black, red, green, yellow, blue, magenta, cyan, white

# 🌈 Bright Variants
# bright_black, bright_red, bright_green, bright_yellow,
# bright_blue, bright_magenta, bright_cyan, bright_white

# 💎 Other Common Named Colors
# grey, gray, orange1, gold1, violet, pink1, deeppink1,
# turquoise2, sky_blue1, dodger_blue2, plum1, purple,
# aquamarine1, spring_green2, chartreuse2, green_yellow
