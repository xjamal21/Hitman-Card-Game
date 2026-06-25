import os

class ScoreManager:
    def __init__(self, db_file="user_database.txt"):
        self.db_file = db_file
        # Automatically ensure the database file exists
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as file:
                pass

    def handle_user_action(self, username):
        username = username.strip()

        players = []
        user_found = False
        new_score = 1

        # 1. Read existing data and check for the user
        with open(self.db_file, "r") as file:
            for line in file:
                if not line.strip():
                    continue
                
                stored_username, stored_score = line.strip().split(",")
                
                if stored_username == username:
                    user_found = True
                    new_score = int(stored_score) + 1
                    players.append(f"{username},{new_score}\n")
                    print(f"Welcome back, {username}! Your score has been updated to {new_score}.")
                else:
                    players.append(line)

        # 2. If it's a new user, register them with an initial score of 1
        if not user_found:
            players.append(f"{username},{new_score}\n")
            print(f"Welcome {username}! New account registered. Your initial score is {new_score}.")

        # 3. Save all data back to the file
        with open(self.db_file, "w") as file:
            file.writelines(players)


# def main():
#     # Instantiate the class
#     manager = ScoreManager()

#     while True:
#         manager.handle_user_action()
#         break

# if __name__ == "__main__":
#     main()