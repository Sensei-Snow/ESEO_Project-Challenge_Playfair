'''
Name: main.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 29/04/2026
Description: This file contains the main function with the structure of the program.
'''

from utils import playfair_alphabet, welcome_screen, ask_algorithm, ask_action, ask_text_valid

def main():
    welcome_screen()
    algorithm_chosen = ask_algorithm()
    action = ask_action()
    # text = ask_text_valid("text_to_encrypt")
    # key = ask_text_valid("key")

if __name__ == "__main__":
    main()