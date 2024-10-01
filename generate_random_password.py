# Python program to generate random password

import random
import string

def generate_password(length=8):

    # defining the characters used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # using the random module
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():

    # password input
    password_length = int(input("Input the desired length of the password: "))

    if password_length:
        password = generate_password(password_length)
    else:
        print("Password length is not defined")
    
    # printing the password
    print(f"The generated password is: {password}")

if __name__ == "__main__":
    main()