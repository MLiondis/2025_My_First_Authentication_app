import sys
import bcrypt


def main():
    while True:
        start = input("Login, Register, or Quit: ").strip().lower()
        if start in ["login", "register", "quit"]:
            if start == "login":
            #logs in with login function
                login()
            elif start == "register":
            #registers in with register function
                Register()
            elif start == "quit":
            #returns to terminal 
                print("Goodbye")
                sys.exit(0)
        print("Please input one of the previous options")

# asks the user to login register or quit
def login():
        global username
        # asks the user for their username or password
        while True:
            username = input("What is your username: ")
            password = input("What is your password: ")
            #opens the txt file for altering
            try:
                with open("plain_text.txt", "r") as file:
                    credentials = [line.strip() for line in file]
                for line in credentials:
                    stored_user, stored_pass = line.split(",")
                    if stored_user == username:
                        if bcrypt.checkpw(password.encode(), stored_pass.encode()):
                            print("Logged in succesfully!")
                            change_password()
                        else:
                            print("Incorrect username or password")
                print("Incorrect username or password")
            except FileNotFoundError:
                print("Error: The file 'plain_text.txt' does not exist.")
                sys.exit(0)

def Register():
    #registers a new password and username
    new_username = input("New username: ")
    while True:
        new_password = input("New password: ")
        if ispasswordvalid(new_password):
            try:
                with open("plain_text.txt", "a") as file:
                    hashed_pass = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
                    #writes the new password and username on a new line
                    file.write(f"\n{new_username},{hashed_pass.decode()}")
            except FileNotFoundError:
                print("Error: The file 'plain_text.txt' does not exist.")
                sys.exit(0)
            print(f"{new_username} has been registered!")
            while True:
                start2 = input("Login or Quit: ").strip().lower()
                if start2 in ["login", "quit"]:
                    if start2 == "login":
                        #logs in wih login function
                        login()
                    elif start2 == "quit":
                        #returns to terminal
                        print("Goobye!")
                        sys.exit(0)


def change_password():
    while True:
        start3 = input("Change password or Quit: ").strip().lower()
        if start3 in ["change password", "quit"]:
            if start3 == "quit":
                print("Goodbye!")
                sys.exit(0)
            elif start3 == "change password":
                new_password = input("New password: ")
                hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
                rows = []
                try:
                    with open("plain_text.txt", "r") as file:
                            for line in file:
                                user, password = line.strip().split(",")
                                if user == username:
                                    rows.append(f"{user},{hashed_password.decode()}")
                                else:
                                    rows.append(line.strip())
                except FileNotFoundError:
                    print("Error: The file 'plain_text.txt' does not exist.")
                    sys.exit(0)
                with open("plain_text.txt", "w") as file:
                    file.write("\n".join(rows) + "\n")
                print("Password changed successfully!")



def ispasswordvalid(password):
    if len(password) < 4:
        print("Password must be at least 4 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return False
    if not any(char.isalpha() for char in password):
        print("Password must contain at least one letter.")
        return False
    return True

main() #cheeky main 