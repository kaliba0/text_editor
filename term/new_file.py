from utilities import Colors, coltxt, input_placeholder
import os


def new_file():

    name = input(coltxt('txteditor/newfile ', Colors.bold)+ coltxt('(name your new file) ') + coltxt('>>> ', Colors.bold))
    
    while True:
        if name=="":
            name = input(coltxt('txteditor/newfile ', Colors.bold)+ coltxt('(name your new file) ') + coltxt('>>> ', Colors.bold))
        else :
            break

    dir_list = os.listdir("../files")
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
