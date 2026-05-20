import cards
import random

class Deck:
    def __init__(self):
        self.decks = []
        
    def build_deck(self, player_count):
        self.decks = [] # reset deck everytime the game restart
        
        # add cards into the deck
        angel_mapping = {2:1, 3:1, 4:2, 5:2, 6:3} # 2-3 players = 1 angel card etc
        num_angel = angel_mapping.get(player_count)
        for _ in range(num_angel):
            self.decks.append(cards.Angel())

        SkipReverseAttack_mapping = {2:4, 3:4, 4:5, 5:5, 6:6}
        num_SkipReverseAttack = SkipReverseAttack_mapping.get(player_count)
        for _ in range(num_SkipReverseAttack):
            self.decks.append(cards.Skip())
            self.decks.append(cards.Reverse())
            self.decks.append(cards.Attack())
        
        FutureShuffleSteal_mapping = {2:2, 3:3, 4:4, 5:5, 6:6}
        num_FutureShuffleSteal = FutureShuffleSteal_mapping.get(player_count)
        for _ in range(num_FutureShuffleSteal):
            self.decks.append(cards.Future())
            self.decks.append(cards.Shuffle())
            self.decks.append(cards.Steal())
        
        BottomSteal_mapping = {2:3, 3:3, 4:4, 5:4, 6:5}
        num_BottomSteal = BottomSteal_mapping.get(player_count)
        for _ in range(num_BottomSteal):
            self.decks.append(cards.Bottom())
            self.decks.append(cards.Steal())
        
        if player_count >= 3:
            superAttack_mapping = {3:1, 4:2, 5:2, 6:3}
            num_superAttack = superAttack_mapping.get(player_count)
            for _ in range(num_superAttack):
                self.decks.append(cards.SuperAttack())
            
            self.decks.append(cards.Clone())
            
        num_hitman = player_count - 1
        for _ in range(num_hitman):
            self.decks.append(cards.Hitman())    
            
        for _ in range(4):
            self.decks.append(cards.Mirror())
            
        # shuffle the deck
        random.shuffle(self.decks)