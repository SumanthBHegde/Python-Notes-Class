#To display if the number is palindrome 

num_final = int(input("Enter a value: "))
num_init = num_final
rev = 0
while(num_final>0):
    dig = num_final%10
    rev = rev*10 + dig
    num_final = num_final // 10

if (num_init):
    print("The value is a palindrome")
else:
    print("The value is not a palindrome")