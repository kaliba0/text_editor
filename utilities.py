import os


class Colors:
    bold = '\033[1m'
    reset= '\033[0m'
    red= '\033[0;31m'
    red_bold = '\033[1;31m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def coltxt(txt, col):
    return col + txt + Colors.reset

def input_placeholder(txt: str, placeholder: str):
