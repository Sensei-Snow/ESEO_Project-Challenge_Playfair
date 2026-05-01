'''
Name: utils.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 01/05/2026
Description: This file contains all the functions related to the user interface of the program, such as the welcome screen, the configuration questions, and the text and key input. It also contains some public variables that are used in other files, such as the alphabet used for the Playfair cipher.
'''

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from InquirerPy import inquirer

#------------------------------------------------------------------------------Public variables
playfair_alphabet = (" ", "!", "'", ",", "-", ".", "?", "@",
                     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                     "_", "§")

#------------------------------------------------------------------------------Private variables

#------------------------------------------------------------------------------Public functions
#---------------------------------------Welcome screen
def welcome_screen():
    print("\n")
    console = Console()
    console.print(Align.center(
        Panel(
            Align.center("\n[bold #ff69b4]Welcome to my tiny message encrypter and decrypter ![/bold #ff69b4]\n"
            "\n[magenta][underline]Description:[/underline] With this little educational tool, you will be able to test the Playfair encryption method.\nIt is only possible to encrypt textual messages with the 26 capital letters of the alphabet and some punctuation.\nOf course it is also possible to use the decryption method.[/magenta]\n"
            "\n[yellow]⚠️ [underline]Warning:[/underline] Seriously, just don't use this project to encrypt important messages... ⚠️[/yellow]\n"),
            title="🌸 Message Encrypter and Decrypter 🌸",
            width=140
            )
        )
    )
    print("\n")
    console.print(Align.center(
        Panel(
            Align.center("\n[magenta][underline]Author:[/underline] Arthur RETAILLAUD E1[/magenta]\n"
                         "[magenta][underline]Contact:[/underline] arthur.retaillaud@reseau.eseo.fr[/magenta]\n"
                         "[magenta][underline]Version:[/underline] Beta[/magenta]\n"
                         "[magenta][underline]License:[/underline] No license needed, just do whatever you want with this thing...[/magenta]\n"),
            title="Project informations",
            width=80
            )
        )
    )

#---------------------------------------Ask configuration
def ask_start():
    print("\n\n")
    console = Console()
    console.print(
        Panel(
            Align.center(
                "\n[bold #ff69b4]Choose the action you want to do[/bold #ff69b4]\n"),
            width=60
        )
    )

    action_chosen = inquirer.select(
        message="\nChoose an action:",
        choices=[
            "Start the program",
            "Check for updates",
            "Exit the program"
        ],
        qmark="",
        pointer="➤ "
    ).execute()

    return action_chosen

def ask_algorithm():
    print("\n\n")
    console = Console()
    console.print(
        Panel(
            Align.center("\n[bold #ff69b4][underline]Step 1:[/underline] Choose the encryption algorithm you want to use[/bold #ff69b4]\n"
                         "[underline]Note:[/underline] New algorithms will be released in the next versions, please be patient.\n"),
            width=60
        )
    )

    algorithm_chosen = inquirer.select(
        message="\nChoose an algorithm:",
        choices=[
            "Playfair"
        ],
        qmark="",
        pointer="➤ "
    ).execute()

    return algorithm_chosen

def ask_action():
    print("\n\n")
    console = Console()
    console.print(
        Panel(
            Align.center("\n[bold #ff69b4][underline]Step 2:[/underline] Choose the action you want to do[/bold #ff69b4]\n"),
            width=60
        )
    )

    action_chosen = inquirer.select(
        message="\nChoose an action:",
        choices=[
            "Encrypt",
            "Decrypt"
        ],
        qmark="",
        pointer="➤ "
    ).execute()

    return action_chosen

#---------------------------------------Ask text and key
def ask_text_valid(parameter):
    valid  = False

    while not valid:
        if parameter == "text_to_encrypt":
            input_text = input("Please enter your text to encrypt: ")
        elif parameter == "key":
            input_text = input("Please enter your key: ")

        input_text_high = input_text.upper()
        len_input_text = len(input_text)
        num_good_chars = 0
        for char in input_text_high:
            if char not in playfair_alphabet:
                print(f"[ERROR] -- Invalid character found in you input text : \"{char.lower()}\"")
            else:
                num_good_chars += 1
        if num_good_chars == len_input_text:
            valid = True

    return input_text_high

#------------------------------------------------------------------------------Private functions