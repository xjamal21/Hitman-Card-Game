import keyboard
import colorama
import time
import random
import string
import os 
from game import Game
from deck import Deck
from colorama import Fore

# welcome screen
print(Fore.RED + r"""
 __    __  ______  ________  __       __   ______   __    __       
|  \  |  \|      \|        \|  \     /  \ /      \ |  \  |  \      
| $$  | $$ \$$$$$$ \$$$$$$$$| $$\   /  $$|  $$$$$$\| $$\ | $$      
| $$__| $$  | $$     | $$   | $$$\ /  $$$| $$__| $$| $$$\| $$      
| $$    $$  | $$     | $$   | $$$$\  $$$$| $$    $$| $$$$\ $$      
| $$$$$$$$  | $$     | $$   | $$\$$ $$ $$| $$$$$$$$| $$\$$ $$      
| $$  | $$ _| $$_    | $$   | $$ \$$$| $$| $$  | $$| $$ \$$$$      
| $$  | $$|   $$ \   | $$   | $$  \$ | $$| $$  | $$| $$  \$$$      
 \$$   \$$ \$$$$$$    \$$    \$$      \$$ \$$   \$$ \$$   \$$      
                                                                   
                                                                   
""")

input("Press ENTER to continue...")

print("Continuing...")
time.sleep(1)

# generate loading screen
chars = string.ascii_letters + string.digits + "/\{}[]<>"

for i in range(30):
    loading = "".join(random.choice (chars) for i in range (30))
    print(loading)
    time.sleep(0.08)

os.system("cls")

# run the game mechanic
current_game = Game()

# create lobby
current_game.create_lobby()

# display player list
print("=========================== PLAYERS ===============================")
print(f" > {current_game}")
print("===================================================================")

# construct the deck based on player count
game_deck = Deck()
game_deck.build_deck(current_game.get_player_count())

# setup game
current_game.setup_game(game_deck.decks)

# start game
current_game.start_game_loop(game_deck.decks)