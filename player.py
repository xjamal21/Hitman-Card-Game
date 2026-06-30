import random
import os
import time
import builtins
import colorama
from colorama import Fore, Style  
from theme import active_theme    

colorama.init(autoreset=False)

def show_error(message):
    os.system("cls")
    builtins.print(f"{Fore.RED}{Style.BRIGHT}ERROR: {message}{Style.RESET_ALL}")
    time.sleep(1)
    os.system("cls")
    builtins.print(active_theme.current_color, end="")

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.turn = 1
        self.isAlive = True
        
    def __repr__(self):
        return self.name
    
    def show_hand(self):
        if self.hand == []:
            show_error("You have no card to play.")
        else:
            for index, card in enumerate(self.hand):
                print(f"[{index}] {card.name:<20} | {card.desc}")
    
    def encounter_assassin(self):
        guard_found = False
        
        for card in self.hand:
            if card.name == "Guard Card":
                self.hand.remove(card)
                guard_found = True
                notice = f"{self.name} drew an Assassin Card but used an Guard Card. The Assassin Card is put back in deck randomly."
                own_notice = "You drew a Assassin Card but used an Guard Card. The Assassin Card is put back in deck randomly."
                return False, notice, own_notice
        
        if not guard_found:
            self.isAlive = False
            notice = f"{self.name} drew an Assassin Card and blew up."
            own_notice = "You drew an Assassin Card. You're dead."
            return True, notice, own_notice
              
    def draw_card(self, deck):
        if deck[0].name == "Assassin Card":
            isDead, notice, own_notice = self.encounter_assassin()
            if isDead:
                deck.pop(0)
                return notice, own_notice
            else:
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
            
    def play_card(self, game, deck, current_player):
        if self.hand == []:
            show_error("You have no card to play.")
            return None
        
        try:
            chosen_card_index = int(input(f"{active_theme.current_color}Enter the card index (0 to {len(self.hand) - 1}): "))

            if chosen_card_index >= len(self.hand) or chosen_card_index < 0:
                os.system("cls")  
                show_error("Invalid input.")
                return None
            
        except ValueError:
            show_error("Invalid input.")
            return None
            
        chosen_card = self.hand[chosen_card_index]   
                        
        if chosen_card.name == "Guard Card":
            os.system("cls")  
            show_error("You cannot use a Guard Card.")
            return None

        card_result = chosen_card.ability(game, deck, current_player)
        if card_result is not None:
            game.discarded_cards.append(chosen_card)
            
            if chosen_card in self.hand:
                self.hand.remove(chosen_card)  
                
        return card_result