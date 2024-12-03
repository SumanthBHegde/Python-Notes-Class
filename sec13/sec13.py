# import required module
from cryptography.fernet import Fernet
key = Fernet.generate_key()

# Generate a key and save it in the same folder
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
# To see the generated key
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print("The generated key: ",key)

# encrypt file
f = Fernet(key)
with open('tips.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('encrypted_tips.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# To see encrypted file contents
file1 = open("encrypted_tips.txt","r+")
print("The encrypted file content ")
print(file1.read())
print()

#decrypt file
with open('encrypted_tips.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)
with open('decrypted_tips.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
    
file1 = open("decrypted_tips.txt","r+")
print("The decrypted file content ")
print(file1.read())
print()