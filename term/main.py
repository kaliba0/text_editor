from utilities import Colors, clear_screen, coltxt
from new_file import new_file
from load_file import load_file
from editor import editor
import sys


RESET = '\033[0m'
BOLD = '\033[1m'


def show_menu():
    banner =  coltxt("""\n\n
TTTTT X   X TTTTT EEEEE DDDD  III TTTTT  OOO  RRRR  
  T    X X    T   E     D   D  I    T   O   O R   R 
  T     X     T   EEEE  D   D  I    T   O   O RRRR  
  T    X X    T   E     D   D  I    T   O   O R  R  
  T   X   X   T   EEEEE DDDD  III   T    OOO  R   R 
                                                    """, Colors.bold)

    menu = "\n\nSelect one of the option below: \n\t1.Create new file\n\t2.Load a file\n"                                                                         

    print(banner)
    print(menu)


def menu_input():
    try:
        option = input(coltxt('txteditor >>> ', Colors.bold))
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(0)

    if option not in ['1', '2']:
        print(coltxt('INCORRECT OPTION CHOOSEN. ', Colors.red_bold) + coltxt('Choose 1 or 2.', Colors.red))
        menu_input()

    if option == '1':
        editor(new_file())


    if option =='2':
        editor(load_file())




def main():
    clear_screen()
    show_menu()
    menu_input()

if __name__=="__main__":
    main()
