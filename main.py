'''
Name: main.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 12/05/2026
Description: This file contains the main function with the structure of the program.
'''

__version__ = "Beta"

from utils import welcome_screen, choose_action_start, choose_algorithm, choose_encrypt_decrypt, choose_text_file, ask_input_text, ask_text_valid, is_input_text_valid, save_text, encrypt, decrypt
from update import is_update_available, ask_update, download_new_version
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from playfair_functions import clear_digrammes

def main():
    welcome_screen()

    action_chosen = choose_action_start()
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

    algorithm_chosen = choose_algorithm()

    action = choose_encrypt_decrypt()

    if action == "Encrypt":
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

        text = ask_input_text()

        key = ask_text_valid("key")

        print("\n")
        encrypt_text = encrypt(algorithm_chosen, text, key)

        print("\n")
        input_method = choose_text_file("output")
        if input_method == "Raw text":
            print(f"\n[INFO] -- Text encrypted : {encrypt_text}")
        else:
            save_text(encrypt_text)

    else:
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

        text = ask_input_text()

        key = ask_text_valid("key")

        print("\n")
        texte_dechiffrer_dirty = decrypt(algorithm_chosen, text, key)
        texte_dechiffrer_clear = clear_digrammes(texte_dechiffrer_dirty)
        texte_minus = texte_dechiffrer_clear.lower()
        texte_dechiffrer = texte_minus.capitalize()

        input_method = choose_text_file("output")
        if input_method == "Raw text":
            print(f"\n[INFO] -- Text decrypted : {texte_dechiffrer}")
        else:
            save_text(texte_dechiffrer)

if __name__ == "__main__":
    main()