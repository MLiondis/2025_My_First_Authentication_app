import sys
# asks the user to login register or quit

def login():
        # asks the user for their username or password
        username = input("What is your username: ")
        password = input("What is your password: ")
        #opens the txt file for altering
        try:
            with open("plain_text.txt", "r") as file:
                for line in file:
                    #splits it into name and password
                    row = line.split(",")
                    check_username = row[0]
                    check_password = row[1]
                    if username in check_username and password in check_password:
                        print("Logged in successfuly!")
                        #changes the password with the function
                        change_password()
                    elif username not in check_username or password not in check_password:
                        print("Incorrect username or passwword")
        except FileNotFoundError:
            print("Error: The file 'plain_text.txt' does not exist.")
            sys.exit(1)

def Register():
    global new_password
    global new_username
    #registers a new password and username
    new_username = input("New username: ")
    while True:
        new_password = input("New password: ")
        if ispasswordvalid(new_password):
            try:
                with open("plain_text.txt", "a") as file:
                    #writes the new password and username on a new line
                    file.write(f"\n{new_username},{new_password}")
            except FileNotFoundError:
                print("Error: The file 'plain_text.txt' does not exist.")
                sys.exit(1)
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
                        sys.exit(1)


def change_password():
    start3 = input("Change password or Quit: ")
    if start3 == "Quit":
        print("Goodbye!")
        sys.exit(1)
    elif start3 == "Change password":
        newest_password = input("New password: ")
        #Pseudocode:
        #open plain_text.txt as file
        #gets the new pasword that the user added and replaces it with the changed one
        #

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
                sys.exit()
        print("Please input one of the previous options")

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