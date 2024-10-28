import requests
import hashlib

# Read the file containing usernames and password
with open('pass.txt', 'r') as f:
    for line in f:
        # Split the line into username and password
        username, password = line.strip().split(',')

        # Hash the password using SHA-1 algorithm
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        # Make a request to 'Have i been pawned' api to check if the password has been leaked
        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

        # if the response status code is 200, it means the password has been leaked
        if response.status_code == 200:
            # Get the link of hashes of leaked passwords that start with the same 5 characters as the input passwords
            hashes = [line.split(':') for line in response.text.splitlines()]

            # Check if the hash of the password matches any of the leaked password hashes
            for h, count in hashes:
                if password_hash[5:] == h:
                    print(f"Password for user {username} has been leaked {count} times.")
                    break
        else:
            print(f"Could not check password for user {username}")
