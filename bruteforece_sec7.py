# Bruteforece attack
import itertools
import string

def bruteforec (password):
    chars = string.printable.strip()
    attempts = 0
    for length in range(len(password), len(password) + 1):
        for guess in itertools.product(chars,repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(guess)
            if guess == password:
                return (attempts, guess)
        return(attempts, None)
    
def main():
    password = input('input the passowrd to crack: ')
    attempts, guess = bruteforec(password) 
    if guess:
        print(f'Password cracked in {attempts} attempts. The password is {guess}')
    else:
        print(f'Password no cracked after {attempts} attempts .')   
    
    
main()