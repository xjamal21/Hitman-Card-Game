# add card name and description and other stuff
# pk add ability
class Card:
    def __init__(self, name, desc, doesSkipTurn):
        self.name = name
        self.desc = desc
        self.doesSkipTurn = doesSkipTurn
        
    def __repr__(self):
        return self.name

class Hitman(Card):
    def __init__(self):
        super().__init__(
            name = "Hitman",
            desc = "You're dead.",
            doesSkipTurn = None
        )
        
class Angel(Card):
    def __init__(self):
        super().__init__(
            name = "Angel Card",
            desc = "Protects you when you draw the Hitman.",
            doesSkipTurn = None
        )

class Skip(Card):
    def __init__(self):
        super().__init__(
            name = "Skip Card",
            desc = "End your turn without drawing a card.",
            doesSkipTurn = True
        )
        
class Future(Card):
    def __init__(self):
        super().__init__(
            name = "Future Card",
            desc = "Secretly view the top 3 cards in the deck.",
            doesSkipTurn = False
        )

class Reverse(Card):
    def __init__(self):
        super().__init__(
            name = "Reverse Card",
            desc = "End your turn and reverse the play order.",
            doesSkipTurn = False
        )

class Attack(Card):
    def __init__(self):
        super().__init__(
            name = "Attack Card",
            desc = "Skip your turn. A player you choose must take 2 turns in his next turn.",
            doesSkipTurn = True
        )
        
class Mirror(Card):
    def __init__(self):
        super().__init__(
            name = "Mirror Card",
            desc = "Copy the effect of the card underneath.",
            doesSkipTurn = None
        )           
        
class Shuffle(Card):
    def __init__(self):
        super().__init__(
            name = "Shuffle Card",
            desc = "Shuffle the deck.",
            doesSkipTurn = False
        )
        
class Inferno(Card):
    def __init__(self):
        super().__init__(
            name = "Inferno Card",
            desc = "Remove the last card copies from all players hands and put them back in the deck.",
            doesSkipTurn = False
        )
        
class Bottom(Card):
    def __init__(self):
        super().__init__(
            name = "Bottom Card",
            desc = "End your turn by drawing from the bottom of the deck.",
            doesSkipTurn = True
        )
        
class SuperAttack(Card):
    def __init__(self):
        super().__init__(
            name = "Super Attack Card",
            desc = "Skip your turn. All other players must take 2 turns.",
            doesSkipTurn = True 
        )

class Clone(Card):
    def __init__(self):
        super().__init__(
            name = "Clone Card",
            desc = "Choose a player, your hand becomes a copy of theirs.",
            doesSkipTurn = False
        )
        
class Steal(Card):
    def __init__(self):
        super().__init__(
            name = "Steal Card",
            desc = "Choose a player, and steal a random card from their hand.",
            doesSkipTurn = False
        )