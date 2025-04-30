# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code provides options for logging in, registering, and quitting, which are essential for a user authentication system.
   - It uses a text file (`plain_text.txt`) to store user credentials, which is a simple way to persist data.

2. **Separation of Concerns**:
   - The code separates functionality into different functions (`login`, `Register`, `change_password`), which is a good practice for modularity.

---

### **Issues and Suggestions for Improvement**

#### 1. **Security Issues**
   - **Plain Text Passwords**: Storing passwords in plain text (`plain_text.txt`) is a significant security risk.
   - **No Password Hashing**: Passwords should be hashed before being stored to protect user data.

   **Fix**: Use a library like `bcrypt` to hash passwords before storing them and verify hashed passwords during login.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 2. **File Handling**
   - The code does not handle file operations robustly:
     - It assumes the file `plain_text.txt` exists and is formatted correctly.
     - It does not handle potential errors, such as the file being missing or corrupted.

   **Fix**: Add error handling for file operations.

   Example:
   ```python
   try:
       with open("plain_text.txt", "r") as file:
           # File operations
   except FileNotFoundError:
       print("Error: The file 'plain_text.txt' does not exist.")
       sys.exit(1)
   ```

---

#### 3. **Logic Errors**
   - **Login Validation**:
     - The `if username in check_username and password in check_password` condition is too permissive. It may incorrectly validate partial matches (e.g., `user` matches `username`).
     - The `elif username not in check_username or password not in check_password` condition is redundant and unnecessary.

   **Fix**: Use exact matches for username and password validation.

   Example:
   ```python
   if username == check_username and password == check_password:
       print("Logged in successfully!")
   else:
       print("Incorrect username or password.")
   ```

   - **Change Password Functionality**:
     - The `change_password` function is incomplete and does not implement the logic to update the password in the file.

   **Fix**: Implement the logic to update the password in the file.

   Example:
   ```python
   def change_password(username):
       new_password = input("Enter a new password: ")
       hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
       rows = []
       with open("plain_text.txt", "r") as file:
           for line in file:
               user, password = line.strip().split(",")
               if user == username:
                   rows.append(f"{user},{hashed_password.decode()}")
               else:
                   rows.append(line.strip())
       with open("plain_text.txt", "w") as file:
           file.write("\n".join(rows) + "\n")
       print("Password changed successfully!")
   ```

---

#### 4. **Code Readability**
   - **Inconsistent Naming**: Function names like `Register` (capitalized) and `login` (lowercase) are inconsistent. Stick to a consistent naming convention (e.g., `snake_case`).
   - **Lack of Comments**: The code lacks sufficient comments to explain the logic in detail.
   - **Global Variables**: The use of `global new_password` is unnecessary and should be avoided.

   **Fix**: Use consistent naming, add comments, and avoid global variables.

---

#### 5. **Input Validation**
   - The code does not validate user input properly. For example:
     - If the user enters an invalid option (e.g., "Loginn"), the program does not handle it gracefully.
     - There is no check for empty or invalid usernames/passwords.

   **Fix**: Add input validation to handle invalid or empty inputs.

   Example:
   ```python
   while True:
       start = input("Login, Register, or Quit: ").strip().lower()
       if start in ["login", "register", "quit"]:
           break
       print("Invalid option. Please choose 'Login', 'Register', or 'Quit'.")
   ```

---

#### 6. **Password Strength**
   - The code does not enforce any password strength requirements (e.g., minimum length, special characters).

   **Fix**: Add basic password strength validation.

   Example:
   ```python
   def is_valid_password(password):
       if len(password) < 6:
           print("Password must be at least 6 characters long.")
           return False
       if not any(char.isdigit() for char in password):
           print("Password must contain at least one number.")
           return False
       if not any(char.isalpha() for char in password):
           print("Password must contain at least one letter.")
           return False
       return True
   ```

---

#### 7. **Quitting the Program**
   - The `sys.exit(1)` calls are unnecessary for normal program termination. Use `sys.exit(0)` or simply `return` to exit gracefully.