import re

def sign_up():
    print("\nWelcome to the Sign-Up Page!\n")
    
    # Get valid username
    while True:
        username = input("Enter a username (max 15 chars, no symbols): ")
        if len(username) > 15:
            print("Error: Username must be 15 characters or less.")
        elif not re.match(r'^[a-zA-Z0-9_]+$', username):
            print("Error: Username can only contain letters, numbers, and underscores.")
        else:
            break
    
    # Get valid age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Error: Age cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number for age.")
    
    # Get valid password
    while True:
        password = input("Enter your password (min 6 chars): ")
        confirm_password = input("Confirm your password: ")
        
        if password != confirm_password:
            print("Error: Passwords do not match.")
        elif len(password) < 6:
            print("Error: Password must be at least 6 characters long.")
        else:
            break
    
    print("\nAccount successfully created!\n")
    return {"username": username, "age": age, "password": password}

# Example usage
if __name__ == "__main__":
    user_data = sign_up()
    print("User Details:", user_data)
