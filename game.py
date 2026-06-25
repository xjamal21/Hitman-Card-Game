from player import Player
import cards
import time
import os
from theme import ThemeManager



class Game:
    def __init__(self):
        self.players = []
        self.taken_names = []
        self.notification = []
        self.direction = 1
        self.discarded_cards = []

        
    def __repr__(self):
        return str(self.players)
    
    def get_player_count(self):
        return len(self.players)    
    
    def create_lobby(self):
        while True:
            name_input = input("Insert your name. Type '1' to start the game (Minimum 2 players): ").strip()

            if name_input == "1":
                if self.get_player_count() < 2:
                    print("Not enough players!")
                else:
                    break
            else:
                if self.get_player_count() >= 6:
                    print("Too many players. Type '1' to start the game:")
                elif name_input.isdigit() or name_input.isspace() or name_input == "":
                    print("Invalid name.")
                elif name_input in self.taken_names:
                    print("Your name has been taken. Insert another name.")
                else:
                    self.players.append(Player(name_input))
                    self.taken_names.append(name_input)
    
    def setup_game(self, deck):
        # Loading screen: setting up game assets
        os.system("cls")
        print("Setting up card deck...")
        time.sleep(0.5)
        print("Distributing protection cards...")
        time.sleep(0.5)
        print("Shuffling remaining cards...")
        time.sleep(0.8)

        os.system("cls")

        for player in self.players:
            player.hand.append(cards.Guard())

            for _ in range(4):
                for card in deck: #skip assassin and proceed to next card
                    if card.name != "Assassin Card":
                        deck.remove(card)
                        player.hand.append(card)
                        break
    
    def get_players_alive(self):
        alive_players = []     
        for player in self.players:
            if player.isAlive:
                alive_players.append(player)
                
        return alive_players
    
    def get_num_assassin(self, deck):
        num = 0
        for card in deck:
            if card.name == "Assassin Card":
                num += 1
        
        return num
    
    def get_chance_assassin(self, deck):
        percentage = (f"{round(self.get_num_assassin(deck) / len(deck) * 100, 2)}%")
        return percentage
    
    def add_notification(self, text, triggered_player):
        self.notification.append({
            "text": text,
            "viewers": [triggered_player]
        })
    
    # display ingame notification
    def display_notification(self, current_player):
        if self.notification != []:
            expired_notice = []
            alive_players = self.get_players_alive()
            
            for notice in self.notification:
                if notice is None:
                    continue
                
                if current_player.name not in notice['viewers']:   
                    print(f"{notice['text']}")
                    notice["viewers"].append(current_player.name)

                doDisplay = False
                for player in alive_players:
                    if player.name not in notice["viewers"]:
                        doDisplay = True
                        break
                        
                if not doDisplay:
                    expired_notice.append(notice)
                    
            for old_notice in expired_notice:
                self.notification.remove(old_notice)
        
    def start_game_loop(self, deck):
        game_over = False
        current_index = 0
        
        print("Game start.")
        
        while not game_over:
            current_player = self.players[current_index]
            
            # skip dead players
            if current_player.isAlive:       
                print("===================================================================")
                print(f"Players Left: {len(self.get_players_alive())} | Assassin Card: {self.get_num_assassin(deck)} | Death Chance: {self.get_chance_assassin(deck)} | Card Left: {len(deck)}")
                self.display_notification(current_player)
                print("===================================================================")
                
                print(f"Now is {current_player.name} turn.")
                
                required_turns = getattr(current_player, "turn")
                turn = 0
                
                # loop turn until player finish required turns
                while turn < required_turns:
                    print(f"Turn {turn + 1} of total {required_turns} turns.")
                    current_player.show_hand()
                    player_choice = input("Take an action. (p) Play a card (d) Draw a card: ").lower()
                    
                    if player_choice == "p":
                        card_result = current_player.play_card(self, deck, current_player)
                        if card_result is not None:     
                            doesSkipTurn, notice, own_notice = card_result
                            # end 1 turn if the card played does skip turn
                            self.add_notification(notice, current_player.name)
                            print(own_notice)
                            
                            if doesSkipTurn:
                                turn += 1
                    elif player_choice == "d":
                        notice, own_notice = current_player.draw_card(deck)
                        self.add_notification(notice, current_player.name)
                        print(own_notice)
                        turn += 1
                    else:
                        os.system("cls")  
                        print("Invalid input. Type 'p' or 'd'.")

                current_player.turn = 1
                
                input("Press ENTER to end your turn...")
                os.system("cls")   

            # end the game if alive players is 1
            if len(self.get_players_alive()) == 1:
                print(f"GAME OVER! {self.get_players_alive()[0]} is the winner!") 
                game_over = True
                break
            
            current_index += self.direction
            current_index = current_index % len(self.players)