'''
Name: update.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 30/04/2026
Date of last modifications: 01/05/2026
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
def is_update_available():
    steps = [
        "Searching local version",
        "Searching remote version",
        "Compare versions"
    ]

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
def extract_version(script):
    for line in script.splitlines():
        if line.startswith("__version__"):
            return line
    return None

def get_remote_version():
    request = requests.get(Remote_MainPy_Url, timeout=5)
    if request.status_code == 200:
        return extract_version(request.text)
    return None

def get_local_version():
    with open("main.py", "r") as local_script:
        return extract_version(local_script.read())