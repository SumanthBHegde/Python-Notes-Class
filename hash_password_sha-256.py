#python program to digest the passwords
import hashlib

def hash_password(password):
    #Ecoding to bytes
    password_byte = password.encode('utf-8')

    #Using SHA-256 for hashing and creating hash object
    hash_object = hashlib.sha256(password_byte)

    #Getting the hexadecimal of the hash
    password_hash = hash_object.hexdigest()
    return password_hash

password = input("Input the password: ")
hashed_password = hash_password(password)
print(f"Your hashed password is: {hashed_password}")

# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/SumanthBHegde/Python-Notes-Class.git
# git push -u origin main