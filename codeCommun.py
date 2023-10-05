#!/bin/env python3

import sys, re



def construire(l0):
    def _construire():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i] == "[":
                i += 1
                if i != 1:
                    l.append(_construire())
            elif l0[i] == "]":
                i += 1
                return l
            else:
                l.append(int(l0[i]))
                i += 1
    i = 1                              # indice pour parcourir les arguments
    return _construire()



def get_list_from_input():
    # code pour récupérer la liste saisi par l'utilisateur
    listes = []
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        line = re.split(r' +',line.rstrip("\n"))
        i = 0
        liste = construire(line)
        listes.append(liste)
    return listes


def get_list_from_file(file_name):
    # code pour recupérer les listes sur un fichier
    f = open(file_name, "r")
    listes = []
    for line in f:
        line = re.split(r' +',line.rstrip("\n"))
        i=0
        liste = construire(line)
        listes.append(liste)
    return listes
