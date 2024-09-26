text = input("Enter the word to check : ")

cnt = 0
for i in text:
    if i in 'aeiou':
        cnt += 1

print(f"The number of vowels are {cnt}")

