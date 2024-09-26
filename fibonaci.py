# Check if the no belongs to the fibonacci sequence

#input the no
n = int(input("Enter the number: "))
temp, a, b = 0, 0, 1
if n==0 and n==1:
    print("Yes it is a fibonacci number")
else:
    while temp < n :
        temp = a+b
        b = a
        a = temp
    
    #After loop termination
    if temp == n:
        print("Yes, it is a fibonacci no")
    else:
        print("No, it is not a fibonacci no")
