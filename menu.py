import keyboard
import msvcrt
import pyfiglet
import colorama
import os

from pyfiglet import figlet_format

options = ["Start Game", "Tutorial", "Settings", "Quit Game"]
selected = 0

while True:
    os.system("cls")

    print(r""" _   _ _____ ________  ___  ___   _   _  
| | | |_   _|_   _|  \/  | / _ \ | \ | | 
| |_| | | |   | | | .  . |/ /_\ \|  \| | 
|  _  | | |   | | | |\/| ||  _  || . ` | 
| | | |_| |_  | | | |  | || | | || |\  | 
\_| |_/\___/  \_/ \_|  |_/\_| |_/\_| \_/ 
                                         
                                         """)
    
    for i, option in enumerate(options):
        if i == selected:
            print(f"> {option}")
        else:
            print(f"  {option}")

    key = msvcrt.getch()

    if key == b'\xe0':
        key = msvcrt.getch()

        if key == b'H':
            selected -= 1

        elif key == b'P':
            selected += 1

    elif key == b'\r':
        print(f"\nYou selected {options[selected]}")
        break

    if selected < 0:
        selected = len(options) - 1

    elif selected >= len(options):
        selected = 0
