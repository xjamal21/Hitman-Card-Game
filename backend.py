# add introduction
# dixon add menu with start setting-language quit and tutorial
# dixon add player alive display, add chances of getting a hitman

import time
import random
import string
import os 
from game import Game
from deck import Deck

# generate loading screen
chars = string.ascii_letters + string.digits + "/\{}[]<>"

for i in range(30):
    loading = "".join(random.choice (chars) for i in range (30))
    print(loading)
    time.sleep(0.08)

os.system("cls")

# run the game mechanic
current_game = Game()

# add player into the list
# try make this to a class method
while True:
    name_input = input("Insert your name (type 'start' to start the game): ")

    if name_input == "start":
        if current_game.get_player_count() < 2:
            print("Not enough players!")
        else:
            break
    else:
        if current_game.get_player_count() >= 6:
            print("Too many players. Insert 'start' to start the game.")
        else:
            current_game.add_player(name_input)

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