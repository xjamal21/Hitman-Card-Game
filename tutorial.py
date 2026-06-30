import os

class TutorialMode:
    def __init__(self):
        self.steps = [
            "Welcome to Killerz! This is a turn-based tactical survival game.",
            "Your main goal? Survive. There are hidden Assassin cards buried deep inside the deck.",
            "Everyone starts the game safely with 5 cards total, including 1 Guard Card in their hand.",
            "On your turn, you have two choices:\n(p) Play a card from your hand to use its ability, or\n(d) Draw a card from the deck.",
            "Be careful! Drawing cards increases your risk. Keep a close eye on the 'Death Chance' percentage on your dashboard.",
            "If you draw an Assassin Card, you are instantly eliminated... UNLESS you discard a Guard Card to protect yourself.",
            "Some cards or effects might force you to take multiple turns in a row! You must finish all required turns before passing.",
            "Use your action cards wisely to skip turns, alter the deck, or sabotage your opponents.",
            "The last player standing wins the game. Good luck, agent!"
        ]

    def run(self):
        for index, text in enumerate(self.steps):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"=================== TUTORIAL ({index + 1}/{len(self.steps)}) ===================\n")
            print(text)
            print("\n===================================================================")
            
            input("\nPress ENTER to continue...")

        os.system("cls" if os.name == "nt" else "clear")
        print("Tutorial complete! You are ready to play.\n")
        input("Press ENTER to return to the main menu...")