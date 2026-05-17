# add card name and description
class Card:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
    def __repr__(self):
        return self.name

class Hitman(Card):
    def __init__(self):
        super().__init__(
            name = "Hitman",
            desc = "You're dead."
        )
        
class Angel(Card):
    def __init__(self):
        super().__init__(
            name = "Angel Card",
            desc = "Protects you when you draw the Hitman."
        )

class Skip(Card):
    def __init__(self):
        super().__init__(
            name = "Skip Card",
            desc = "End your turn without drawing a card."
        )
        
class Future(Card):
    def __init__(self):
        super().__init__(
            name = "Future",
            desc = "Secretly view the top 3 cards in the deck."
        )

class Reverse(Card):
    def __init__(self):
        super().__init__(
            name = "Reverse Card",
            desc = "End your turn and reverse the play order."
        )

class Attack(Card):
    def __init__(self):
        super().__init__(
            name = "Attack Card",
            desc = "Skip your turn. A player you choose must take 2 turns in his next turn."
        )
        
class Mirror(Card):
    def __init__(self):
        super().__init__(
            name = "Mirror Card",
            desc = "Copy the effect of the card underneath."
        )           
        
class Shuffle(Card):
    def __init__(self):
        super().__init__(
            name = "Shuffle Card",
            desc = "Shuffle the deck."
        )
        
class Inferno(Card):
    def __init__(self):
        super().__init__(
            name = "Inferno Card",
            desc = "Remove the last card copies from all players hands and put them back in the deck."
        )
        
class Bottom(Card):
    def __init__(self):
        super().__init__(
            name = "Bottom Card",
            desc = "End your turn by drawing from the bottom of the deck."
        )
        
class SuperAttack(Card):
    def __init__(self):
        super().__init__(
            name = "Super Attack Card",
            desc = "All other players must take 2 turns."
        )

class Clone(Card):
    def __init__(self):
        super().__init__(
            name = "Clone Card",
            desc = "Choose a player, your hand becomes a copy of theirs."
        )