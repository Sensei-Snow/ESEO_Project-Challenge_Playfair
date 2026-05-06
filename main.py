'''
Name: main.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 06/05/2026
Description: This file contains the main function with the structure of the program.
'''

__version__ = "Beta"

from utils import playfair_alphabet, welcome_screen, ask_start, ask_algorithm, ask_action, ask_text_valid, encrypt, decrypt
from update import is_update_available, ask_update, download_new_version
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
# from playfair_functions import creerGrille, indicesDansGrille, afficherGrille, creerDigrammes, chiffrerDigrammes, dechiffrerDigrammes

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

    match action:
        case "Encrypt":
            print("\n\n")
            console = Console()
            console.print(
                Panel(
                    Align.center(
                        "\n[bold #ff69b4][underline]Step 3:[/underline] Encrypt the text[/bold #ff69b4]\n"),
                    width=60
                )
            )
            print("\n")
            text = ask_text_valid("text_to_encrypt")
            key = ask_text_valid("key")
            print("\n")
            encrypt(algorithm_chosen, text, key)
        case "Decrypt":
            print("\n\n")
            console = Console()
            console.print(
                Panel(
                    Align.center(
                        "\n[bold #ff69b4][underline]Step 3:[/underline] Decrypt the text[/bold #ff69b4]\n"),
                    width=60
                )
            )
            print("\n")
            text = ask_text_valid("text_to_decrypt")
            key = ask_text_valid("key")
            print("\n")
            decrypt(algorithm_chosen, text, key)

if __name__ == "__main__":
    main()