from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)
msg = 'have a nice day'.encode()
encrypted_msg = fernet.encrypt(msg)
decrypted_msg = fernet.decrypt(encrypted_msg)
decrypted_msg = decrypted_msg.decode()
#print all msg
print('originial msg :: ',msg.decode())
print('Encrypted msg : ', encrypted_msg)
print('Decrypted msg : ', decrypted_msg)