import requests
import random
import time
from colorama import Fore

while True:
    user = ""
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890_", k=4):
        user = user + character

    url = f"https://www.instagram.com/{user}/"
    response = requests.get(url)

    if f'"{user}"' in response.text:
        print(Fore.RED + f"USER FOUND: {user}" + Fore.RESET)
    else:
        print(Fore.GREEN + f"NOT FOUND: {user}" + Fore.RESET)
    time.sleep(2)
