#Find the sum of n natural numbers

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    #using loop to iterate 
    for i in range(num):
        n = i+1
        sum += n

#printing the sum
print(f"The sum of {num} is {sum}")