'''
Name: update.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 30/04/2026
Date of last modifications: 13/05/2026
Description: This file contains the main function with the structure of the program.
'''

import requests
from tqdm import tqdm
import time
from InquirerPy import inquirer

#------------------------------------------------------------------------------Public variables

#------------------------------------------------------------------------------Private variables
Remote_MainPy_Url = "https://raw.githubusercontent.com/Sensei-Snow/ESEO_Project-Challenge_Playfair/main/main.py"
Repository_Zip_Url = "https://github.com/Sensei-Snow/ESEO_Project-Challenge_Playfair/archive/refs/heads/main.zip"

#------------------------------------------------------------------------------Public functions
'''
Brief: Vérifie si une mise à jour est disponible en comparant la version locale du script avec la version distante sur GitHub.
Return [bool]: True si une mise à jour est disponible, False sinon.
'''
def is_update_available():
    steps = [
        "Searching local version",
        "Searching remote version",
        "Compare versions"
    ]

    local_version = ""
    remote_version = ""

    for step in tqdm(steps, desc="Checking updates"):
        if step == "Searching local version":
            local_version = get_local_version()
            tqdm.write(f"[INFO] -- Local version : {local_version}")
            time.sleep(0.5)
        elif step == "Searching remote version":
            remote_version = get_remote_version()
            tqdm.write(f"[INFO] -- Remote version : {remote_version}")
            time.sleep(0.5)
        elif step == "Compare versions":
            tqdm.write("[INFO] -- Comparing versions...")
            time.sleep(0.5)

    if local_version != remote_version:
        print("\n[INFO] -- Update available")
        return True
    else:
        print("\n[INFO] -- Update not available")
        return False

'''
Brief: Demande à l'utilisateur s'il souhaite télécharger automatiquement ou manuellement la nouvelle version
Return [str]: Le texte associé à l'action voulue
'''
def ask_update():
    action_chosen = inquirer.select(
        message="\nChoose an action:",
        choices=[
            "Download new version",
            "Promise to check my GitHub later",
        ],
        qmark="",
        pointer="➤ "
    ).execute()

    return action_chosen

'''
Brief: Télécharge la nouvelle version du projet sur le GitHub
'''
def download_new_version():
    print("\n[INFO] -- Connecting to server")
    response = requests.get(Repository_Zip_Url, stream=True, timeout=5)

    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 1024  # 1 KB

    print("[INFO] -- Downloading new version")
    with open("new_version.zip", "wb") as f, tqdm(
            desc="Download",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
                time.sleep(0.01)

#------------------------------------------------------------------------------Private functions
'''
Brief: Regarde la version actuelle du projet en local
Parameter (script) [str]: The script that contains the version 
Return [str|None]: La version du projet 
'''
def extract_version(script):
    for line in script.splitlines():
        if line.startswith("__version__"):
            return line
    return None

'''
Brief: Regarde la version actuelle du projet sur GitHub
Return [str|None]: La version du projet sur GitHub
'''
def get_remote_version():
    request = requests.get(Remote_MainPy_Url, timeout=5)
    if request.status_code == 200:
        return extract_version(request.text)
    return None

'''
Brief: Regarde la version actuelle du projet en local
Return [str|None]: La version du projet en local
'''
def get_local_version():
    with open("main.py", "r") as local_script:
        return extract_version(local_script.read())