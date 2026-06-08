import colorama
from colorama import Fore

colorama.init(autoreset=True)

class ThemeManager:
    def __init__(self):
        self.themes = [
            ("Default (White)", Fore.WHITE),
            ("Hacker Green", Fore.GREEN),
            ("Blood Red", Fore.RED),
            ("Neon Blue", Fore.BLUE),
            ("Cyber Yellow", Fore.YELLOW),
            ("Magenta Mist", Fore.MAGENTA)
        ]
        self.current_name = "Default (White)"
        self.current_color = Fore.WHITE