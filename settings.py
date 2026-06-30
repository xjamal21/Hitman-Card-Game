import os
import msvcrt
import time
from theme import ThemeManager
from theme import active_theme

class SettingsMenu:
    def __init__(self):
        self.theme = active_theme
        self.options = ["Change Theme", "Back to Menu"]
        self.selected = 0

    def open(self):
        """Main settings routing loop."""
        while True:
            os.system("cls")
            print(self.theme.current_color + "=== SETTINGS ===")
            print(f"Current Theme: {self.theme.current_name}\n")

            for i, option in enumerate(self.options):
                if i == self.selected:
                    print(self.theme.current_color + f"> {option}")
                else:
                    print(f"  {option}")

            key = msvcrt.getch()

            if key == b'\xe0':
                key = msvcrt.getch()
                if key == b'H':    
                    self.selected -= 1
                elif key == b'P':  
                    self.selected += 1

            elif key == b'\r':     
                choice = self.options[self.selected]
                
                if choice == "Change Theme":
                    self.open_theme_selector()
                elif choice == "Back to Menu":
                    break

            if self.selected < 0:
                self.selected = len(self.options) - 1
            elif self.selected >= len(self.options):
                self.selected = 0

    def open_theme_selector(self):
        """Sub-menu displaying available color configurations."""
        theme_idx = 0
        while True:
            os.system("cls")
            print(self.theme.current_color + "=== SELECT A THEME ===")
            
            for i, (name, _) in enumerate(self.theme.themes):
                if i == theme_idx:
                    print(self.theme.current_color + f"> {name}")
                else:
                    print(f"  {name}")
                    
            print("\n[Press ENTER to select | Press ESC to cancel]")

            
            key = msvcrt.getch()

            if key == b'\xe0':
                key = msvcrt.getch()
                if key == b'H':
                    theme_idx -= 1
                elif key == b'P':
                    theme_idx += 1
    
            elif key == b'\r':
                self.theme.current_name, self.theme.current_color = self.theme.themes[theme_idx]
                print(self.theme.current_color + f"\nTheme applied: {self.theme.current_name}!")
                time.sleep(1)
                break
                
            elif key == b'\x1b': 
                break

            if theme_idx < 0:
                theme_idx = len(self.theme.themes) - 1
            elif theme_idx >= len(self.theme.themes):
                theme_idx = 0