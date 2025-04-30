import sys
# asks the user to login register or quit
start = input("Login, Register, or Quit: ")

def login():
    while True:
        # asks the user for their username or password
        username = input("What is your username: ")
        password = input("What is your password: ")
        #opens the txt file for altering
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

def Register():
    global new_password
    #registers a new password and username
    new_username = input("New username: ")
    new_password = input("New password: ")
    with open("plain_text.txt", "a") as file:
        #writes the new password and username on a new line
        file.write(f"\n{new_username},{new_password}")
    print(f"{new_username} has been registered!")
    start2 = input("Login or Quit: ")
    if start2 == "Login":
        #logs in wih login function
        login()
    elif start2 == "Quit":
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

if start == "Login":
    #logs in with login function
    login()
elif start == "Register":
    #registers in with register function
    Register()
elif start == "Quit":
    #returns to terminal 
    print("Goodbye")
    sys.exit(1)