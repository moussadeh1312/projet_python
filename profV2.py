#!/bin/env python3

from codeCommun import *

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Aucun argument sur la ligne de commande, demander interactivement à l'utilisateur.
        list_generator = get_list_from_input()
    elif len(sys.argv) == 2:
        # Un argument unique est fourni sur la ligne de commande, c'est le nom du fichier.
        file_name = sys.argv[1]
        list_generator = get_list_from_file(file_name)
    else:
        # Les arguments fournissent directement la liste à traiter.
        list_generator = [construire(sys.argv[1:])]

    for l in list_generator:
        print(f"{l=}")
        print(f"{profondeur(l)=}")