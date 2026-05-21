#  notice when someone draws a hitman card or when someone dies

from player import Player
import cards
import os

class Game:
    def __init__(self):
        self.players = []
        self.taken_names = []
        self.notification = []
        
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
        # dixon add some loading screen like setting up blablabla
        for player in self.players:
            player.hand.append(cards.Angel())

            for _ in range(4):
                for card in deck: #skip hitman and proceed to next card
                    if card.name != "Hitman":
                        deck.remove(card)
                        player.hand.append(card)
                        break
        # dixon send a msg like setup complete everyone has 5 cards
    
    def get_players_alive(self):
        alive_players = []     
        for player in self.players:
            if player.isAlive:
                alive_players.append(player)
                
        return alive_players
    
    def get_num_hitman(self, deck):
        num = 0
        for card in deck:
            if card.name == "Hitman":
                num += 1
        
        return num
    
    def get_chance_hitman(self, deck):
        percentage = (f"{round(self.get_num_hitman(deck) / len(deck) * 100, 2)}%")
        return percentage
    
    def add_notification(self, text, player_got_hitman):
        self.notification.append({
            "text": text,
            "viewers": [player_got_hitman]
        })
    
    # display notice when someone got hitman or when someone died
    def display_notification(self, current_player):
        if self.notification != []:
            expired_notice = []
            alive_players = self.get_players_alive()
            
            for notice in self.notification:
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
        
        print("Game start.")
        
        while not game_over:
            for current_player in self.players:
                # skip dead players
                if not current_player.isAlive:  
                    continue
                
                print("===================================================================")
                print(f"Players Left: {len(self.get_players_alive())} | Hitman: {self.get_num_hitman(deck)} | Death Chance: {self.get_chance_hitman(deck)} | Card Left: {len(deck)}")
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
                        played_card = current_player.play_card()
                        if played_card is not None:
                            # end 1 turn if the card played does skip turn
                            if played_card.doesSkipTurn:
                                turn += 1
                    elif player_choice == "d":
                        current_player.draw_card(deck, self)
                        turn += 1
                    else:
                        os.system("cls")  
                        print("Invalid input. Type 'p' or 'd'.")

                input("Press ENTER to end your turn...")
                os.system("cls")   

                # end the game if alive players is 1
                if len(self.get_players_alive()) == 1:
                    print(f"GAME OVER! {self.get_players_alive()[0]} is the winner!") 
                    game_over = True
                    break