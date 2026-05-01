'''
Name: main.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 01/05/2026
Description: This file contains the main function with the structure of the program.
'''

__version__ = "Beta"

from utils import playfair_alphabet, welcome_screen, ask_start, ask_algorithm, ask_action, ask_text_valid
from update import is_update_available, ask_update, download_new_version
from playfair_encrypt_functions import creerGrille, indicesDansGrille, afficherGrille, creerDigrammes


def main():
    welcome_screen()

    action_chosen = ask_start()
    match action_chosen:
        case "Check for updates":
            print("\n")
            if is_update_available():
                action_chosen = ask_update()
                if action_chosen == "Download new version":
                    download_new_version()
        case "Exit the program":
            print("\nThank you for visiting. We hope to see you again soon.")
            exit()

    algorithm_chosen = ask_algorithm()
    action = ask_action()

if __name__ == "__main__":
    # main()

    # text = ask_text_valid("text_to_encrypt")
    # key = ask_text_valid("key")
    # divided_tab = creerGrille(key, playfair_alphabet, True)
    # complete_tab = creerGrille(key, playfair_alphabet, False)
    # print(divided_tab)
    # print(complete_tab)
    #
    # char = "B"
    # print(indicesDansGrille(char, divided_tab))
    #
    # afficherGrille(divided_tab)

    print(creerDigrammes("Hello..."))