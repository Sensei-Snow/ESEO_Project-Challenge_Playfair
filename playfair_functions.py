'''
Name: playfair_functions.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 06/05/2026
Description: This file contains all the functions related to the Playfair encryption method.
'''

def creerGrille(passphrase, playfair_alphabet, divided_tab):
    tab = []

    for char in passphrase:
        if char not in tab:
            tab.append(char)

    for char in playfair_alphabet:
        if char not in tab:
            tab.append(char)

    if divided_tab:
        return [tab[i:i + 6] for i in range(0, len(tab), 6)]
    else:
        return tab

def indicesDansGrille(char, tab):
    line = 0
    column =0

    character_found = False

    while not character_found:
        if not character_found and  line < 6:
            if not character_found and column < 6:
                if tab[line][column] == char:
                    character_found = True
                else:
                    column += 1
            else:
                if not character_found:
                    line += 1
                    column = 0
        else:
            if character_found:
                return (line, column)
            else:
                return None

    return (line, column)

def afficherGrille(tab):
    for line in tab:
        print(* line, sep=" ")

def creerDigrammes(text):
    upper_text = text.upper()

    digrammes_tab = []

    tab_text = list(upper_text)

    actual_char = 0
    while actual_char < len(tab_text):
        try:
            if tab_text[actual_char] == tab_text[actual_char+1]:
                actual_digramme = (tab_text[actual_char], "§")
                digrammes_tab.append(actual_digramme)
                actual_char += 1
            else:
                actual_digramme = (tab_text[actual_char], tab_text[actual_char+1])
                digrammes_tab.append(actual_digramme)
                actual_char += 2
        except:
            actual_digramme = (tab_text[actual_char], "§")
            digrammes_tab.append(actual_digramme)
            actual_char += 1

    return digrammes_tab

def chiffrerDigrammes(digramme_tab, tab):
    chiffrer_tab = []

    for digramme in digramme_tab:
        coordonnees1 = indicesDansGrille(digramme[0], tab)
        coordonnees2 = indicesDansGrille(digramme[1], tab)

        if coordonnees1[0] == coordonnees2[0]:
            try:
                new_character1 = tab[coordonnees1[0]][coordonnees1[1]+1]
            except:
                new_character1 = tab[coordonnees1[0]][coordonnees1[1]-5]

            try:
                new_character2 = tab[coordonnees2[0]][coordonnees2[1]+1]
            except:
                new_character2 = tab[coordonnees2[0]][coordonnees2[1]-5]

            digramme_chiffrer = (new_character1, new_character2)

        elif coordonnees1[1] == coordonnees2[1]:
            try:
                new_character1 = tab[coordonnees1[0]+1][coordonnees1[1]]
            except:
                new_character1 = tab[coordonnees1[0]-5][coordonnees1[1]]

            try:
                new_character2 = tab[coordonnees2[0]+1][coordonnees2[1]]
            except:
                new_character2 = tab[coordonnees2[0]-5][coordonnees2[1]]

            digramme_chiffrer = (new_character1, new_character2)

        else:
            new_character1 = tab[coordonnees1[0]][coordonnees2[1]]
            new_character2 = tab[coordonnees2[0]][coordonnees1[1]]

            digramme_chiffrer = (new_character1, new_character2)

        chiffrer_tab.append(digramme_chiffrer)

    return chiffrer_tab

def dechiffrerDigrammes(digramme_chiffrer_tab, tab):
    dechiffrer_tab = []

    for digramme in digramme_chiffrer_tab:
        coordonnees1 = indicesDansGrille(digramme[0], tab)
        coordonnees2 = indicesDansGrille(digramme[1], tab)

        if coordonnees1[0] == coordonnees2[0]:
            try:
                new_character1 = tab[coordonnees1[0]][coordonnees1[1]-1]
            except:
                new_character1 = tab[coordonnees1[0]][coordonnees1[1]+5]

            try:
                new_character2 = tab[coordonnees2[0]][coordonnees2[1]-1]
            except:
                new_character2 = tab[coordonnees2[0]][coordonnees2[1]+5]

            digramme_chiffrer = (new_character1, new_character2)

        elif coordonnees1[1] == coordonnees2[1]:
            try:
                new_character1 = tab[coordonnees1[0]-1][coordonnees1[1]]
            except:
                new_character1 = tab[coordonnees1[0]+5][coordonnees1[1]]

            try:
                new_character2 = tab[coordonnees2[0]-1][coordonnees2[1]]
            except:
                new_character2 = tab[coordonnees2[0]+5][coordonnees2[1]]

            digramme_chiffrer = (new_character1, new_character2)

        else:
            new_character1 = tab[coordonnees1[0]][coordonnees2[1]]
            new_character2 = tab[coordonnees2[0]][coordonnees1[1]]

            digramme_chiffrer = (new_character1, new_character2)

        dechiffrer_tab.append(digramme_chiffrer)

    return dechiffrer_tab