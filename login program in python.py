users = {"user1": "password1", "user2": "password2"}


def validate_login(username, password):
    # Check the username and password together
    return users.get(username) == password


def login():
    # Prompt the user for login details
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if validate_login(username, password):
        print("Login successful!")
    else:
        print("Username or password is incorrect.")


# Example usage
login()
