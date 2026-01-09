import os
from utilities import Colors, coltxt
import pathlib

term_dir = pathlib.Path(__file__).resolve().parent
project_dir = term_dir.parent
files_dir = project_dir / "files"

def load_file():

    liste_fichier = os.listdir(files_dir)
    n = 0
    options = []
    for i in range(len(liste_fichier)) :
        n += 1
        options.append(n)
        print(f"\t {n}.{liste_fichier[i]}")
    reponse = ""
    while not validite_entree(reponse, options) :
        reponse = input(coltxt('txteditor/loadfile', Colors.bold) + coltxt(' (type the file number) ', Colors.grey) + coltxt('>>> ', Colors.bold))

    return liste_fichier[int(reponse)-1].split('.')[-2]



def validite_entree(reponse, options) :
    critere = True
    if reponse == "" :
        return False
    try :
        reponse = int(reponse)
    except :
        print(coltxt('INCORRECT OPTION CHOSEN. ', Colors.red_bold) + coltxt('Choose a number.', Colors.red))
        critere = False
    else :
        if int(reponse) not in options :
            print(coltxt('INCORRECT OPTION CHOSEN. ', Colors.red_bold) + coltxt('Choose a valid number.', Colors.red))
            critere = False
    return critere