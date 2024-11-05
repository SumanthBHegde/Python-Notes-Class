# Finding largest number in a list

mylist = []
size = int(input("Enter the size of the list: "))

print(f"Enter {size} elements: ")
for i in range(size):
    element = int(input("Enter element: "))
    mylist.append(element)
    
mylist.sort()
print(f"Largest Element is {mylist[-1]}")