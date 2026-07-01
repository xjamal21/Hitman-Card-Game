import os
import msvcrt
import time
from theme import ThemeManager
from theme import active_theme
from login import ScoreManager

class SettingsMenu:
    def __init__(self):
        self.theme = active_theme
        self.options = ["Change Theme", "Edit Scoreboard", "Back to Menu"]
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
                elif choice == "Edit Scoreboard":
                    self.edit_score()
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
                
    def edit_score(self):
        score_idx = 0
        scoreboard = ScoreManager()
        
        while True:
            os.system("cls")
            print(self.theme.current_color + "=== SCOREBOARD ===")
            
            score_list = scoreboard.display_score()

            if len(score_list) == 0:
                print(self.theme.current_color + "[The scoreboad is empty]")
                print("\n[Press ESC to return to Settings]")
            else:
                for i, score in enumerate(score_list):
                    if i == score_idx:
                        print(self.theme.current_color + f"> {score.strip()}")
                    else:
                        print(f"  {score.strip()}")
                
                
                print("\n[Press ENTER to delete | Press DELETE to clear all scores | Press ESC to cancel]")
            
            key = msvcrt.getch()

            if key == b'\xe0':
                key = msvcrt.getch()
                if len(score_list) > 0:
                    if key == b'H':
                        score_idx -= 1
                    elif key == b'P':
                        score_idx += 1
                    elif key == b'S':
                        scoreboard.clear_all_scores()
    
            elif key == b'\r':
                if len(score_list) > 0:
                    scoreboard.delete_score(score_idx)
                    print(self.theme.current_color + "Score deleted.")
                    time.sleep(1)
                
            elif key == b'\x1b': 
                break

            if len(score_list) > 0:
                if score_idx < 0:
                    score_idx = len(score_list) - 1
                elif score_idx >= len(score_list):
                    score_idx = 0
            else:
                score_idx = 0