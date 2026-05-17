# add introduction
import time
import random
import string
import os 

chars = string.ascii_letters + string.digits + "/\{}[]<>"

for i in range(50):
    loading = "".join(random.choice (chars) for i in range (50))
    print(loading)
    time.sleep(0.08)

os.system("cls")

player_list = []


while True:
    name_input = input("Insert your name (type 'start' to start the game): ")

    if name_input != "start":
        player_list.append(name_input)
    else:
        if len(player_list) < 2:
            print("Not enough players!")
        elif len(player_list) >= 6:
            print("Too many players. Insert 'start' to start the game.")
        else:
            break

print("=========================== PLAYERS ===============================")

print(f" > {player_list}")

print("===================================================================")


