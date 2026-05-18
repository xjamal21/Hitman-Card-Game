from player import Player
import cards

class Game:
    def __init__(self):
        self.players = []
        
    def __repr__(self):
        return str(self.players)
    
    def add_player(self, name):
        self.players.append(Player(name))
        
    def player_count(self):
        return len(self.players)
    
    def setup_game(self, deck):
        # dixon add some loading screen like setting up blablabla
        for player in self.players:
            player.hand.append(cards.Angel())

            for _ in range(4):
                for card in deck: #skip hitman and proceed to next card
                    if card != "Hitman":
                        deck.remove(card)
                        player.hand.append(card)
                        print(player.hand)
                        break
        # smth like setup complete everyone has 5 cards