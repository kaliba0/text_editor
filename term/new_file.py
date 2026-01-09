from utilities import Colors, coltxt
import os
import pathlib

term_dir = pathlib.Path(__file__).resolve().parent
project_dir = term_dir.parent
files_dir = project_dir / "files"


def new_file():

    name = input(coltxt('txteditor/newfile ', Colors.bold)+ coltxt('(name your new file) ', Colors.grey) + coltxt('>>> ', Colors.bold))
    
    while True:
        if name=="":
            name = input(coltxt('txteditor/newfile ', Colors.bold)+ coltxt('(name your new file) ', Colors.grey) + coltxt('>>> ', Colors.bold))
        else :
            break

    dir_list = os.listdir(files_dir)
    if f"{name}.txt" in dir_list:
        opt = input(coltxt('Existing file with this name found. Overwrite ? ', Colors.red_bold) + coltxt('(y/n) ', Colors.red))
        while True:
            if opt == 'y':
                f = open(f"../files/{name}.txt", "w")
                break
            elif opt == 'n':
                f = open(f'../files/{name}.txt')
                break
            else:
                opt = input(coltxt('INCORRECT OPTION CHOOSEN. ', Colors.red_bold) + coltxt("Choose 'y' or 'n'. ", Colors.red))
    else :
        f = open(f"../files/{name}.txt", "x")


    return name
