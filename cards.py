import random

class Card:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
    def __repr__(self):
        return self.name
    
    def ability(self, game, deck, current_player):
        pass

class Hitman(Card):
    def __init__(self):
        super().__init__(
            name = "Assassin",
            desc = "Death is upon you."
        )
        
class Angel(Card):
    def __init__(self):
        super().__init__(
            name = "Guard",
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
        
class Future(Card):
    def __init__(self):
        super().__init__(
            name = "Destiny",
            desc = "Look at the top 3 cards in the deck."
        )
        
    def ability(self, game, deck, current_player):
        notice = f"{current_player} used Destiny."
        own_notice = f"The first 3 cards are {deck[0]}, {deck[1]} and {deck[2]}."
        return False, notice, own_notice

class Reverse(Card):
    def __init__(self):
        super().__init__(
            name = "Switch",
            desc = "End your turn and change the game direction."
        )
        
    def ability(self, game, deck, current_player):
        game.direction *= -1
        notice = f"{current_player} changed the play order."
        own_notice = "You changed the play order."
        return True, notice, own_notice

class Attack(Card):
    def __init__(self):
        super().__init__(
            name = "Target",
            desc = "Skip your turn and choose a victim to take an extra turn."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player to attack (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
            target_player.turn += 1
            
            notice = f"{current_player.name} attacked and forced {target_player.name} to take 1 more turn."
            own_notice = f"You forced {target_player.name} to take 1 more turn."
            return True, notice, own_notice
        except (ValueError, IndexError):
            print("Invalid input.")
            return None
        
class Mirror(Card):
    def __init__(self):
        super().__init__(
            name = "Mimic",
            desc = "Use the power of the last card played."
        )          
        
    def ability(self, game, deck, current_player):
        discard_cards = getattr(game, "discarded_cards")
        if discard_cards == []:
            print("No card to mimic.")
            return None
        else:
            last_played_card = discard_cards[-1]
            print(f"Mimic got the ability of {last_played_card.name}.")
            return last_played_card.ability(game, deck, current_player)
        
class Shuffle(Card):
    def __init__(self):
        super().__init__(
            name = "Scramble",
            desc = "Shuffles the deck."
        )
        
    def ability(self, game, deck, current_player):
        random.shuffle(deck)
        notice = f"{current_player} shuffled the deck."
        own_notice = "You shuffled the deck."
        return False, notice, own_notice
        
class Inferno(Card):
    def __init__(self):
        super().__init__(
            name = "Incinerate",
            desc = "Removes all cards that match the last played card from everyone's card."
        )
    
    def ability(self, game, deck, current_player):
        discard_cards = getattr(game, "discarded_cards")
        if discard_cards == []:
            print("No card to burn.")
            return None
        else:
            last_played_card = discard_cards[-1]
            
            for player in game.players:
                card_to_keep = []
                
                for card in player.hand:
                    if last_played_card.name != card.name:
                        card_to_keep.append(card)
                player.hand = card_to_keep
            
            notice = f"{current_player} burned all {last_played_card} from everyone's hand."
            own_notice = f"You burned all {last_played_card} from everyone's hand."    
            return False, notice, own_notice   
        
class Bottom(Card):
    def __init__(self):
        super().__init__(
            name = "Bottom Card",
            desc = "End your turn by drawing from the bottom of the deck."
        )
        
    def ability(self, game, deck, current_player):
        bottom_card = deck[-1]
        if bottom_card.name == "Hitman":
            isDead, notice, own_notice = game.encounter_hitman()
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
        
class SuperAttack(Card):
    def __init__(self):
        super().__init__(
            name = "MassAttack",
            desc = "Skip your turn and everyone must take an extra turn."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for player in alive_players:
            player.turn += 1
        
        notice = f"{current_player} attacked and forced everyone to take 1 more turn."
        own_notice = "You attacked and forced everyone to take 1 more turn."
        return True, notice, own_notice

class Clone(Card):
    def __init__(self):
        super().__init__(
            name = "Copy",
            desc = "Choose a player and make your hand exactly like theirs."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        cloned_hand = []
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player to copy his hand (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
            for card in target_player.hand:
                cloned_hand.append(card)
                
            current_player.hand = cloned_hand
            
            notice = f"{current_player.name} copy {target_player.name}'s hand."
            own_notice = f"You copy {target_player.name}'s hand."
            return True, notice, own_notice
        except (ValueError, IndexError):
            print("Invalid input.3")
            return None
        
class Steal(Card):
    def __init__(self):
        super().__init__(
            name = "Thief",
            desc = "Choose a player and take a random card from them."
        )
        
    def ability(self, game, deck, current_player):
        alive_players = game.get_players_alive()
        alive_players.remove(current_player)
        
        for index, player in enumerate(alive_players):
            print(f"[{index}] {player.name}")
            
        try:
            target = int(input(f"Choose a player to steal a random card from his hand (0-{len(alive_players) - 1}): "))
            target_player = alive_players[target]
   
            chosen_card = random.choice(target_player.hand)
            target_player.hand.remove(chosen_card)
            current_player.hand.append(chosen_card)
            
            notice = f"{current_player.name} stole a card from {target_player.name}'s hand."
            own_notice = f"You stole {chosen_card} from {target_player.name}'s hand."
            return True, notice, own_notice
        except (ValueError, IndexError):
            print("Invalid input.3")
            return None