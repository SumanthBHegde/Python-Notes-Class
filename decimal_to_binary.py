#Program to convert decimal to binary 
number = int(input("Enter a positive number: "))
binary = 0
i = 0
num = number
print(bin(number)[2:])
while num > 0:
    rem = num % 2
    binary = binary + rem*10**i
    i = i+1
    num = num//2

print(f"Binary representation of {number} is {binary}")