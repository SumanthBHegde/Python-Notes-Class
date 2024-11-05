def encrypt(text, s):
    result = ""
    
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 25 + 65)
        
        # Encrypt lowecase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    
    return result

# The main Program
text = "HELLO"
s = 3
print("Plain Text: "+text)
print("Shift pattern: "+ str(s))
print("Cipher: " + encrypt(text,s))