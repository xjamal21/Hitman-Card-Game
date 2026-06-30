import keyboard
import colorama
import time
import random
import string
import os 
from game import Game
from deck import Deck
from menu import GameMenu
from colorama import Fore

colorama.init(autoreset=True)

os.system("cls")

print(Fore.RED + r"""
    
 __    __  ______  __        __        ________ 
|  \  /  \|      \|  \      |  \      |        \
| $$ /  $$ \$$$$$$| $$      | $$       \$$$$$$$$
| $$/  $$   | $$  | $$      | $$          /  $$ 
| $$  $$    | $$  | $$      | $$         /  $$  
| $$$$$\    | $$  | $$      | $$        /  $$   
| $$ \$$\  _| $$_ | $$_____ | $$_____  /  $$___ 
| $$  \$$\|   $$ \| $$     \| $$     \|  $$    \
 \$$   \$$ \$$$$$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$$$
                                                                                                                
                                                                   
""")

input("Press ENTER to continue...")

print("Continuing...")
time.sleep(0.5)

chars = string.ascii_letters + string.digits 
for i in range(30):
    loading = "".join(random.choice(chars) for _ in range(30))
    print(loading)
    time.sleep(0.04)

os.system("cls" if os.name == "nt" else "clear")

menu = GameMenu()   
menu.start()