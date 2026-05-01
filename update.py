'''
Name: update.py
Author: Arthur RETAILLAUD E1
Contact: arthur.retaillaud@reseau.eseo.fr
Date of creation: 30/04/2026
Date of last modifications: 30/04/2026
Description: This file contains the main function with the structure of the program.
'''

import requests

#------------------------------------------------------------------------------Public variables

#------------------------------------------------------------------------------Private variables
Repository_Url = "https://raw.githubusercontent.com/Sensei-Snow/ESEO_Project-Challenge_Playfair/main/main.py"

#------------------------------------------------------------------------------Public functions
def get_remote_version():
    request = requests.get(Repository_Url, timeout=5)
    if request.status_code == 200:
        return extract_version(request.text)
    return None

def get_local_version():
    with open("main.py", "r") as local_script:
        return extract_version(local_script.read())

#------------------------------------------------------------------------------Private functions
def extract_version(script):
    for line in script.splitlines():
        if line.startswith("__version__"):
            return line.split("=")[1].strip().strip('"\'')
    return None