import random
from player import show_error

class Card:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
    def __repr__(self):
        return self.name
    
    def ability(self, game, deck, current_player):
        pass

class Assassin(Card):
    def __init__(self):
        super().__init__(
            name = "Assassin Card",
            desc = "Death is upon you."
        )
        
class Guard(Card):
    def __init__(self):
        super().__init__(
            name = "Guard Card",
            desc = "Protects you from the Assassin."
        )

class Skip(Card):
    def __init__(self):
        super().__init__(
            name = "Skip Card",
            desc = "End your turn without drawing a card."
        )
        
    def ability(self, game, deck, current_player):
        notice = f"{current_player} skipped his turn."
        own_notice = "You skipped your turn."
        return True, notice, own_notice
        
class Destiny(Card):
    def __init__(self):
        super().__init__(
            name = "Destiny Card",
            desc = "Look at the top cards in the deck."
        )
        
    def ability(self, game, deck, current_player):
        if deck == []:
            show_error("The deck is empty.")
            return None
        
        top_cards = deck[:3]
        name_list = []
        
        for card in top_cards:
            name_list.append(card.name)
            
        card_names = ", ".join(name_list)    
        
        notice = f"{current_player} used Destiny."
        own_notice = f"The top cards are {card_names}."
        return False, notice, own_notice

class Switch(Card):
    def __init__(self):
        super().__init__(
            name = "Switch Card",
            desc = "End your turn and change the game direction."
        )
        
    def ability(self, game, deck, current_player):
        game.direction *= -1
        notice = f"{current_player} changed the play order."
        own_notice = "You changed the play order."
        return True, notice, own_notice

class Target(Card):
    def __init__(self):
        super().__init__(
            name = "Target Card",
            desc = "Skip your turn and choose a victim to take an extra turn."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player to target (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
            target_player.turn += 1
            
            notice = f"{current_player.name} targeted and forced {target_player.name} to take 1 more turn."
            own_notice = f"You forced {target_player.name} to take 1 more turn."
            return True, notice, own_notice
        except (ValueError, IndexError):
            show_error("Invalid input.")
            return None
        
class Mimic(Card):
    def __init__(self):
        super().__init__(
            name = "Mimic Card",
            desc = "Use the power of the last card played."
        )          
        
    def ability(self, game, deck, current_player):
        discard_cards = getattr(game, "discarded_cards")
        if discard_cards == []:
            show_error("No card to mimic.")
            return None
    
        last_played_card = discard_cards[-1]
        
        if last_played_card.name == "Mimic Card":
            show_error("A Mimic Card cannot copy another Mimic Card.")
            return None
        
        print(f"Mimic Card copied the ability of {last_played_card.name}.")
        return last_played_card.ability(game, deck, current_player)
        
class Scramble(Card):
    def __init__(self):
        super().__init__(
            name = "Scramble Card",
            desc = "Shuffles the deck."
        )
        
    def ability(self, game, deck, current_player):
        random.shuffle(deck)
        notice = f"{current_player} shuffled the deck."
        own_notice = "You shuffled the deck."
        return False, notice, own_notice
        
class Incinerate(Card):
    def __init__(self):
        super().__init__(
            name = "Incinerate Card",
            desc = "Removes all cards that match the last played card from everyone's card."
        )
    
    def ability(self, game, deck, current_player):
        discard_cards = getattr(game, "discarded_cards")
        if discard_cards == []:
            show_error("No card to remove.")
            return None
        else:
            last_played_card = discard_cards[-1]
            
            for player in game.players:
                card_to_keep = []
                
                for card in player.hand:
                    if last_played_card.name != card.name:
                        card_to_keep.append(card)
                player.hand = card_to_keep
            
            notice = f"{current_player} removed all {last_played_card} from everyone's hand."
            own_notice = f"You removed all {last_played_card} from everyone's hand."    
            return False, notice, own_notice   
        
class Bottom(Card):
    def __init__(self):
        super().__init__(
            name = "Bottom Card",
            desc = "End your turn by drawing from the bottom of the deck."
        )
        
    def ability(self, game, deck, current_player):
        bottom_card = deck[-1]
        if bottom_card.name == "Assassin Card":
            isDead, notice, own_notice = current_player.encounter_assassin()
            if isDead:
                deck.pop(-1)
                return True, notice, own_notice
            else:
                deck.pop(-1)
                random_index = random.randint(0, len(deck))
                deck.insert(random_index, bottom_card)
                return True, notice, own_notice
        else:
            current_player.hand.append(deck[-1])
            deck.pop(-1)
            notice = f"{current_player.name} drew a {bottom_card.name} from the bottom of the deck."
            own_notice = f"You drew a {bottom_card.name} from the bottom of the deck."
            return True, notice, own_notice
        
class MassTarget(Card):
    def __init__(self):
        super().__init__(
            name = "Mass Target Card",
            desc = "Skip your turn and everyone must take an extra turn."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for player in alive_players:
            player.turn += 1
        
        notice = f"{current_player} targeted and forced everyone to take an extra turn."
        own_notice = "You targeted and forced everyone to take an extra turn."
        return True, notice, own_notice

class Copy(Card):
    def __init__(self):
        super().__init__(
            name = "Copy Card",
            desc = "Choose a player and make your hand exactly like theirs."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        copied_hand = []
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player to copy his hand (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
            for card in target_player.hand:
                copied_hand.append(card)
                
            current_player.hand = copied_hand
            
            notice = f"{current_player.name} copied {target_player.name}'s hand."
            own_notice = f"You copied {target_player.name}'s hand."
            return True, notice, own_notice
        except (ValueError, IndexError):
            show_error("Invalid input.")
            return None
        
class Thief(Card):
    def __init__(self):
        super().__init__(
            name = "Thief Card",
            desc = "Choose a player and take a random card from them."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player and take a random card from his hand (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
   
            chosen_card = random.choice(target_player.hand)
            target_player.hand.remove(chosen_card)
            current_player.hand.append(chosen_card)
            
            notice = f"{current_player.name} took a card from {target_player.name}'s hand."
            own_notice = f"You took {chosen_card} from {target_player.name}'s hand."
            return False, notice, own_notice
        except (ValueError, IndexError):
            show_error("Invalid input.")
            return None