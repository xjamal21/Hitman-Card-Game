from player import Player
import cards

class Game:
    def __init__(self):
        self.players = []
        
    def __repr__(self):
        return str(self.players)
    
    def add_player(self, name):
        self.players.append(Player(name))
        
    def get_player_count(self):
        return len(self.players)
    
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
        
    def start_game_loop(self, deck):
        game_over = False
        
        print("Game start.")
        
        while not game_over:
            for current_player in self.players:
                # skip dead players
                if not current_player.isAlive:  
                    continue
                
                print(f"Now is {current_player.name} turn.")
                
                required_turns = getattr(current_player, "turn")
                turn = 0
                
                # loop turn until player finish required turns
                while turn < required_turns:
                    print(f"Turn {turn + 1} of total {required_turns} turns.")
                    current_player.show_hand()
                    player_choice = input("Take an action. (p) Play a card (d) Draw a card: ")
                    
                    if player_choice == "p":
                        played_card = current_player.play_card()
                        if played_card is not None:
                            # end 1 turn if the card played does skip turn
                            if played_card.doesSkipTurn:
                                turn += 1
                    elif player_choice == "d":
                        current_player.draw_card(deck)
                        turn += 1
                    else:
                        print("Invalid input. Type 'p' or 'd'.")
            
                # detect numbers of players alive
                alive_players = []     
                for player in self.players:
                    if player.isAlive:
                        alive_players.append(player)
                
                # end the game if alive players is 1
                if len(alive_players) == 1:
                    print(f"GAME OVER! {alive_players[0]} is the winner!") 
                    game_over = True
                    break          