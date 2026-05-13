'''
Name: main.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 12/05/2026
Description: This file contains the main function with the structure of the program.
'''

__version__ = "V1.0.0"

from utils import welcome_screen, choose_action_start, choose_algorithm, choose_encrypt_decrypt, ask_input_text, ask_output_text, ask_text_valid, encrypt, decrypt
from update import is_update_available, ask_update, download_new_version
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

'''
Brief: La fonction principale du programme exécutée en première
'''
def main():
    # Écran d'accueil
    welcome_screen()

    # Choix de l'action au démarrage
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

    # Choix de l'algorithme
    algorithm_chosen = choose_algorithm()

    # Choix de 'action à exécuter avec l'algorithme
    action_chosen = choose_encrypt_decrypt()

    # Chiffrement
    if action_chosen == "Encrypt":
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

        text_input = ask_input_text("input", "text_to_encrypt")

        key = ask_text_valid("key")

        print("\n")
        encrypt_text = encrypt(algorithm_chosen, text_input, key)

        print("\n")
        ask_output_text(encrypt_text)

    # Déchiffrement
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

        text_input = ask_input_text("input", "text_to_decrypt")

        key = ask_text_valid("key")

        decrypt_text = decrypt(algorithm_chosen, text_input, key)

        print("\n")
        ask_output_text(decrypt_text)

if __name__ == "__main__":
    main()