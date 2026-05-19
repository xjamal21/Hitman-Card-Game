import random

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
                print(f"[{index}] {card.name:<15} | {card.desc}")
    
    # run mechanic when encounter hitman card
    def encounter_hitman(self):
        print(f"{self.name} drawed a Hitman.") #dixon
        angel_found = False
        
        # check whether an angel card is presence in the player hand
        for card in self.hand:
            if card.name == "Angel Card":
                # remove the angel card
                self.hand.remove(card)
                angel_found = True
                print(f"{self.name} used an angel card. The Hitman is put back in deck.") # dixon
                break
        
        # set player to dead if angel card is not present
        if not angel_found:
            self.isAlive = False
            print(f"{self.name} is dead.") #dixon
            return True
              
    # draw card from deck 
    def draw_card(self, deck):
        # run encounter hitman method when the card drawed is hitman
        if deck[0].name == "Hitman":
            isDead = self.encounter_hitman()
            if isDead:
                # remove hitman card when the player is dead
                deck.pop(0)
            else:
                # reposition hitman card in the deck when the player has angel card
                reposition_hitman = deck[0]
                deck.pop(0)
                random_index = random.randint(0, len(deck))
                deck.insert(random_index, reposition_hitman)
        else:
            self.hand.append(deck[0])
            deck.pop(0)
            print(f"You drawed a {self.hand[-1].name}")
            print(self.hand)  # dixon this is print player hand after they drawed a card
            
    # play a card in hand
    def play_card(self):
        if self.hand == []:
            # skip when theres no card in hand
            print("You have no cards to play.")
            return None
        else:
            try:
                # select a card
                chosen_card_index = int(input(f"Enter the card index (0 to {len(self.hand) - 1}): "))
                chosen_card = self.hand[chosen_card_index]  
                 
                if chosen_card_index >= len(self.hand):
                    print("Please input a valid number.")
                    return None
                
                if chosen_card.name == "Angel Card":
                    print("You cannot use an Angel Card.")
                    return None

                self.hand.pop(chosen_card_index)
                # chosen_card.ability()
                return chosen_card
            
            except ValueError:
                print("Please input a valid number.")