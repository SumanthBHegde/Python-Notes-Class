#Program to find the count of the integer is negative, positive or zero 
pos = 0
neg = 0
zero = 0
while True:
    num = int(input("Enter a number (999 to exit): "))
    if num == 999:
        break
    elif num > 0:
        pos = pos+1
    elif num < 0:
        neg = neg+1
    else:
        zero = zero+1
    
print(f"\nPositve Numbers:{pos}")
print(f"\nPositve Numbers:{neg}")
print(f"\nPositve Numbers:{zero}")