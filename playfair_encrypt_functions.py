'''
Name: playfair_encrypt_functions.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 01/05/2026
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