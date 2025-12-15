import os
from utilities import Colors, coltxt, input_placeholder
import pathlib

def load_file():
    p = pathlib.Path('../files')
    liste_fichier = os.listdir(p)
    n = 0
    options = []
    for i in range(len(liste_fichier)) :
        n += 1
        options.append(n)
        print(f"\t {n}.{liste_fichier[i]}")
    reponse = ""
    while not validite_entree(reponse, options) :
        reponse = input("Choisissez un fichier :")

    return liste_fichier[int(reponse)-1].split('.')[-2]



def validite_entree(reponse, options) :
    critere = True
    if reponse == "" :
        return False
    try :
        reponse = int(reponse)
    except :
        print(coltxt('INCORRECT OPTION CHOOSEN. ', Colors.red_bold) + coltxt('Choose a number.', Colors.red))
        critere = False
    else :
        if int(reponse) not in options :
            print(coltxt('INCORRECT OPTION CHOOSEN. ', Colors.red_bold) + coltxt('Choose a valid number.', Colors.red))
            critere = False
    return critere