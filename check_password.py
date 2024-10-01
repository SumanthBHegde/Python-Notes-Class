# Program to check the validity of the password

import re

def validate_password(password):

    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False, f"{password}'s length is less than 8."
    
    # Check if the password has at least one uppercase
    if not re.search(r'[A-Z]', password):
        return False, f"{password} has no upper case charactes"
    
    # Check if the password has at least one lowercase
    if not re.search(r'[a-z]', password):
        return False, f"{password} has no lower case charactes"
    
    # Check if the password has at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, f"{password} has no special charactes"
    
    # Check if the password has at least one uppercase
    if not re.search(r'\d', password):
        return False, f"{password} has no digits"
    
    # All the conditions are satisfied
    return True, f"{password} works!!"

def main():
    password = input("Enter a password: ")
    is_valid, response = validate_password(password)

    if is_valid:
        print("Valid Password.")
    else:
        print(f"Password doesn't meet the the requirements. {response}")

if __name__ == '__main__':
    main()