'''
Name: utils.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 29/04/2026
Date of last modifications: 13/05/2026
Description: This file contains all the functions related to the user interface of the program, such as the welcome screen, the configuration questions, and the text and key input. It also contains some public variables that are used in other files, such as the alphabet used for the Playfair cipher.
'''

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from InquirerPy import inquirer
from playfair_functions import creerGrille, creerDigrammes, chiffrerDigrammes, dechiffrerDigrammes
import os

#------------------------------------------------------------------------------Public variables
playfair_alphabet = (" ", "!", "'", ",", "-", ".", "?", "@",
                     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                     "_", "§")

#------------------------------------------------------------------------------Private variables

#------------------------------------------------------------------------------Public functions
#---------------------------------------Welcome screen
'''
Brief: Affiche un écran de bienvenue
'''
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
    print("\n")
    console.print(Align.center(
        Panel(
            Align.center("\n[magenta][underline]To all people that were following me and watching me on Twitch during the programmation of this project[/underline][/magenta]\n"
                         "\n[magenta]yoongi_sama7[/magenta]\n"
                         "[magenta]chockinyan[/magenta]\n"
                         "[magenta]xhister[/magenta]\n"
                         "[magenta]un_nain_tello[/magenta]\n"
                         "[magenta]kajy44[/magenta]\n"
                         "[magenta]symsym_1629[/magenta]\n"
                         "[magenta]Toinou_DEV[/magenta]\n"),
            title="Thanks !",
            width=80
            )
        )
    )

#---------------------------------------Ask configuration
'''
Brief: Demande à l'utilisateur ce qu'il souhaite faire au démarrage du programme
Return [str]: Le texte associé à l'action voulue
'''
def choose_action_start():
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

'''
Brief: Demande à l'utilisateur l'algorithme de chiffrement qu'il souhaite utiliser
Return [str]: Le texte associé au chiffrement voulu
'''
def choose_algorithm():
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

'''
Brief: Demande à l'utilisateur l'action à exécuter avec l'algorithme
Return [str]: Le texte associé à l'action voulue
'''
def choose_encrypt_decrypt():
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

#---------------------------------------User encryption/decryption configuration
'''
Brief: Demande à l'utilisateur la méthode qu'il veut utiliser pour utiliser son texte
Return [str]: Le texte associé à la méthode voulue
'''
def choose_text_file(parameter):
    if parameter == "input":
        panel_text = "\n[bold #ff69b4]Choose the input method for original text[/bold #ff69b4]\n"
    else:
        panel_text = "\n[bold #ff69b4]Choose the output method for new text[/bold #ff69b4]\n"

    console = Console()
    console.print(
        Panel(
            Align.center(panel_text),
            width=60
        )
    )

    method_chosen = inquirer.select(
        message="\nChoose an action:",
        choices=[
            "Raw text",
            "File input"
        ],
        qmark="",
        pointer="➤ "
    ).execute()

    return method_chosen

'''
Brief: Demande à l'utilisateur un texte en entrée via une entrée ou un fichier puis vérifie la validité du texte
Return [str]: Le texte à utiliser
'''
def ask_input_text(parameter_choose_text_file, parameter_ask_text_valid):
    text = ""
    method_chosen = choose_text_file(parameter_choose_text_file)
    if method_chosen == "Raw text":
        print("\n")
        text = ask_text_valid(parameter_ask_text_valid)
    else:
        while True:
            path = input("\nEnter the file path: ")
            try:
                if os.path.exists(path):
                    with open(path, 'r') as file:
                        text = file.read()
                    if is_input_text_valid(text):
                        break
                    else:
                        continue
            except:
                print("\n[ERROR] -- The file path does not exist")
                continue
    return text

'''
Brief: Exécute la bonne action de sortie
Parameter (text) [str]: Le texte à utiliser
'''
def ask_output_text(text):
    input_method = choose_text_file("output")
    if input_method == "Raw text":
        print(f"\n[INFO] -- Text decrypted : {text}")
    else:
        save_text(text)

'''
Brief: Enregistre le texte de sortie dans un fichier
Parameter (text) [str]: Le texte de sortie à enregistrer
'''
def save_text(text):
    print("\n[INFO] -- Save the text to file output.txt")
    with open("output.txt", 'w') as file:
        file.write(text)

#---------------------------------------Ask text and key
'''
Brief: Demande à l'utilisateur d'entrer un texte qui sera ensuite vérifier
Parameter (parameter) [str]: Décrit l'entrée utilisateur souhaitée
Return [str]: Le texte en majuscule, prêt à être utilisé
'''
def ask_text_valid(parameter):
    valid  = False
    input_text = ""

    while not valid:
        if parameter == "text_to_encrypt":
            input_text = input("Please enter your text to encrypt: ")
        elif parameter == "text_to_decrypt":
            input_text = input("Please enter your text to decrypt: ")
        else:
            input_text = input("Please enter your key: ")

        valid = is_input_text_valid(input_text)

    return input_text.upper()

#---------------------------------------Encrypt and decrypt
'''
Brief: Chiffre un texte avec une clé grâce à une méthode de chiffrement
Parameter (algorithm) [str]: L'algorithme choisi
Parameter (text) [str]: Le texte à chiffrer
Parameter (key) [str]: La clé de chiffrement
Return [str]: Le texte chiffré
'''
def encrypt(algorithm_chosen, text, key):
    match algorithm_chosen:
        case "Playfair":
            print("[INFO] -- Creating tab")
            tab = creerGrille(key, playfair_alphabet, True)
            print("[INFO] -- Creating digrammes")
            digrammes_tab = creerDigrammes(text)
            print("[INFO] -- Encrypting digrammes")
            chiffrer_tab = chiffrerDigrammes(digrammes_tab, tab)

            return ''.join(str(element) for ligne in chiffrer_tab for element in ligne)

'''
Brief: Déchiffre un texte avec une clé grâce à une méthode de chiffrement
Parameter (algorithm) [str]: L'algorithme choisi
Parameter (text) [str]: Le texte à déchiffrer
Parameter (key) [str]: La clé de chiffrement
Return [str]: Le texte déchiffré
'''
def decrypt(algorithm_chosen, text_chiffrer, key):
    match algorithm_chosen:
        case "Playfair":
            print("[INFO] -- Creating tab")
            tab = creerGrille(key, playfair_alphabet, True)
            print("[INFO] -- Creating digrammes")
            digrammes_tab = creerDigrammes(text_chiffrer)
            print("[INFO] -- Decrypting digrammes")
            dechiffrer_tab = dechiffrerDigrammes(digrammes_tab, tab)

            decrypt_text_dirty = ''.join(str(element) for ligne in dechiffrer_tab for element in ligne)
            decrypt_text_clear = decrypt_text_dirty.replace('§', '')
            decrypt_text_minus = decrypt_text_clear.lower()
            return decrypt_text_minus.capitalize()

#------------------------------------------------------------------------------Private functions
'''
Brief: Vérifie la validité d'un texte
Parameter (text) [str]: Le texte à vérifier
Return [bool]: True si le texte est valide, False sinon
'''
def is_input_text_valid(text):
    input_text_high = text.upper()
    for char in input_text_high:
        if char not in playfair_alphabet:
            print(f"\n[ERROR] -- Invalid character found in you input text : \"{char.lower()}\"")
            return False
    return True