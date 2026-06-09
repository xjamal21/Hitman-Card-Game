import cards
import random

class Deck:
    def __init__(self):
        self.decks = []
        
    def build_deck(self, player_count):
        self.decks = [] # reset deck everytime the game restart
        
        # add cards into the deck
        GuardIncinerate_mapping = {2:1, 3:1, 4:2, 5:2, 6:3} # 2-3 players = 1 guard card etc
        num_GuardIncinerate = GuardIncinerate_mapping.get(player_count)
        for _ in range(num_GuardIncinerate):
            self.decks.append(cards.Guard())
            self.decks.append(cards.Incinerate())

        SkipSwitchTarget_mapping = {2:4, 3:4, 4:5, 5:5, 6:6}
        num_SkipSwitchTarget = SkipSwitchTarget_mapping.get(player_count)
        for _ in range(num_SkipSwitchTarget):
            self.decks.append(cards.Skip())
            self.decks.append(cards.Switch())
            self.decks.append(cards.Target())
        
        DestinyScramble_mapping = {2:2, 3:3, 4:4, 5:5, 6:6}
        num_DestinyScramble = DestinyScramble_mapping.get(player_count)
        for _ in range(num_DestinyScramble):
            self.decks.append(cards.Destiny())
            self.decks.append(cards.Scramble())
        
        BottomThief_mapping = {2:3, 3:3, 4:4, 5:4, 6:5}
        num_BottomThief = BottomThief_mapping.get(player_count)
        for _ in range(num_BottomThief):
            self.decks.append(cards.Bottom())
            self.decks.append(cards.Thief())
        
        if player_count >= 3:
            massTarget_mapping = {3:1, 4:2, 5:2, 6:3}
            num_massTarget = massTarget_mapping.get(player_count)
            for _ in range(num_massTarget):
                self.decks.append(cards.MassTarget())
            
            self.decks.append(cards.Copy())
            
        num_assassin = player_count - 1
        for _ in range(num_assassin):
            self.decks.append(cards.Assassin())    
            
        for _ in range(4):
            self.decks.append(cards.Mimic())
            
        # shuffle the deck
        random.shuffle(self.decks)