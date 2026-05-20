import os
import msvcrt

options = ["Play", "Settings", "Tutorial", "Quit"]
selected = 0

while True:
    os.system("cls")

    print("=== HITMAN CARD GAME ===\n")

    for i, option in enumerate(options):
        if i == selected:
            print(f"> {option}")
        else:
            print(f"  {option}")

    key = msvcrt.getch()

    # Arrow keys
    if key == b'\xe0':
        key = msvcrt.getch()

        # UP
        if key == b'H':
            selected -= 1

        # DOWN
        elif key == b'P':
            selected += 1

    # ENTER
    elif key == b'\r':
        print(f"\nYou selected {options[selected]}")
        break

    # Keep selection inside range
    if selected < 0:
        selected = len(options) - 1

    elif selected >= len(options):
        selected = 0