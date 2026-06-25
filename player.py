import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.turn = 1
        self.isAlive = True
        
    def __repr__(self):
        return self.name
    
    # display player hand
    def show_hand(self):
        if self.hand == []:
            print("You have no cards to play.")
        else:
            for index, card in enumerate(self.hand):
                print(f"[{index}] {card.name:<20} | {card.desc}")
    
    # run mechanic when encounter assassin card
    def encounter_assassin(self):
        guard_found = False
        
        # check whether an guard card is presence in the player hand
        for card in self.hand:
            if card.name == "Guard Card":
                # remove the guard card
                self.hand.remove(card)
                guard_found = True
                notice = f"{self.name} drew an Assassin Card but used an Guard Card. The Assassin Card is put back in deck randomly."
                own_notice = "You drew a Assassin Card but used an Guard Card. The Assassin Card is put back in deck randomly."
                return False, notice, own_notice
        
        # set player to dead if guard card is not present
        if not guard_found:
            self.isAlive = False
            notice = f"{self.name} drew an Assassin Card and blew up."
            own_notice = "You drew an Assassin Card. You're dead."
            return True, notice, own_notice
              
    # draw card from deck 
    def draw_card(self, deck):
        # run encounter assasin method when the card drew is assassin
        if deck[0].name == "Assassin Card":
            isDead, notice, own_notice = self.encounter_assassin()
            if isDead:
                # remove assassin card when the player is dead
                deck.pop(0)
                return notice, own_notice
            else:
                # reposition assassin card in the deck when the player has guard card
                reposition_assassin = deck[0]
                deck.pop(0)
                random_index = random.randint(0, len(deck))
                deck.insert(random_index, reposition_assassin)
                return notice, own_notice
        else:
            self.hand.append(deck[0])
            deck.pop(0)
            notice = f"{self.name} drew a {self.hand[-1].name}."
            own_notice = f"You drew a {self.hand[-1].name}."
            return notice, own_notice
            
    # play a card in hand
    def play_card(self, game, deck, current_player):
        if self.hand == []:
            # skip when theres no card in hand
            print("You have no cards to play.")
            return None
        
        try:
            # select a card
            chosen_card_index = int(input(f"Enter the card index (0 to {len(self.hand) - 1}): "))

            if chosen_card_index >= len(self.hand):
                os.system("cls")  
                print("Invalid input.1")
                return None
            
        except ValueError:
            print("Invalid input.2")
            return None
            
        chosen_card = self.hand[chosen_card_index]   
                        
        if chosen_card.name == "Guard Card":
            os.system("cls")  
            print("You cannot use an Guard Card.")
            return None

        card_result = chosen_card.ability(game, deck, current_player)
        if card_result is not None:
            game.discarded_cards.append(chosen_card)
            
            if chosen_card in self.hand:
                self.hand.remove(chosen_card)  
                
        return card_result