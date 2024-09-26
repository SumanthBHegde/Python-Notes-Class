#Program to Multiply the no

number = int(input("Enter a number for multiplication table : "))

print("The multiplication Table of: ",number)
for i in range(1,11):
    print(number,"x",i,'=',number*i)