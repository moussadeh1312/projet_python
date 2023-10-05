#!/bin/env python3

from codeCommun import *

def tri(l):
    # code pour la fonction tri
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

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
        tri(l)
        print(f"{l=}")