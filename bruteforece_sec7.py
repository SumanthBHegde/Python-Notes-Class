import itertools
import string

def bruteforce_attack(password):
    chars = string.printable.strip()
    # print(chars)
    attempts = 0
    for length in range(len(password), len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return (attempts, guess)
    return(attempts, None)

# Main Program
password = input("Input the password to crack: ")
attempts, guess = bruteforce_attack(password)

if guess:
    print(f"Password cracked in {attempts} attempts. The password is {guess}")
else:
    print(f"Password not cracked after {attempts} attempts.")