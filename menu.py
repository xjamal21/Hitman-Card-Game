import keyboard
import msvcrt
import pyfiglet
import colorama
import os
import time
import random
import string
from game import Game
from deck import Deck
from settings import SettingsMenu 
from pyfiglet import figlet_format

class GameMenu:
    def __init__(self):
        self.option1 = "Start Game"
        self.option2 = "Tutorial"
        self.option3 = "Settings"
        self.option4 = "Quit Game"

        self.options = ["Start Game", "Tutorial", "Settings", "Quit Game"]
        self.selected = 0
        
        self.settings = SettingsMenu()

    def start(self):
        while True:
            os.system("cls")

            current_color = self.settings.theme.current_color

            print(current_color + r""" _   _ _____ ________  ___  ___   _   _  
| | | |_   _|_   _|  \/  | / _ \ | \ | | 
| |_| | | |   | | | .  . |/ /_\ \|  \| | 
|  _  | | |   | | | |\/| ||  _  || . ` | 
| | | |_| |_  | | | |  | || | | || |\  | 
\_| |_/\___/  \_/ \_|  |_/\_| |_/\_| \_/ 
                                         
                                         """)
            
            for i, option in enumerate(self.options):
                if i == self.selected:
                    print(current_color + f"> {option}")
                else:
                    print(f"  {option}")

            key = msvcrt.getch()

            if key == b'\xe0':
                key = msvcrt.getch()

                if key == b'H':
                    self.selected -= 1
                elif key == b'P':
                    self.selected += 1

            elif key == b'\r':
                choice = self.options[self.selected]

                if choice == "Start Game":
                    current_game = Game()
                    print(current_color + f"\nYou selected {choice}")
                    current_game.create_lobby()
                    
                    os.system("cls")
                    print(current_color + "Creating lobby and loading game assets...")
                    chars = string.ascii_letters + string.digits + "/\{}[]<>"
                    for _ in range(30):
                        loading = "".join(random.choice(chars) for _ in range(30))
                        print(current_color + loading)
                        time.sleep(0.04)
                    os.system("cls")

                    print("=========================== PLAYERS ===============================")
                    print(f" > {current_game}")
                    print("===================================================================")

                    game_deck = Deck()
                    game_deck.build_deck(current_game.get_player_count())
                    current_game.setup_game(game_deck.decks)
                    current_game.start_game_loop(game_deck.decks)

                elif choice == "Settings":
                    self.settings.open()

                elif choice == "Quit Game":
                    break

            if self.selected < 0:
                self.selected = len(self.options) - 1
            elif self.selected >= len(self.options):
                self.selected = 0