import os

class Colors:
    bold = '\033[1m'
    reset= '\033[0m'
    red= '\033[0;31m'
    red_bold = '\033[1;31m'
    grey="\033[38;2;160;160;160m"
    grey_bold="\033[1;38;2;160;160;160m"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class ColoredTxt:
    def __init__(self, text, color=Colors.reset):
        self.content = color + text + Colors.reset

    def __str__(self):
        return self.content

def coltxt(txt, col= Colors.reset):
    return col + txt + Colors.reset