#Program to print the floyd triangle
n = int(input("Enter the total number of rows: "))
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count," ", end='')
        count = count+1
    print()