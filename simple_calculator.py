#simple calculator of +,-,8,/

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b
def ask():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    return num1,num2

while True:
    print("\nPlease select the operation: \n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Devide\n 5. Exit")
    choice = int(input("Please enter valid choice: "))
    
    if choice == 1:
        num1, num2 = ask()
        print(add(num1,num2))
    elif choice == 2:
        num1, num2 = ask()
        print(subtract(num1,num2))
    elif choice == 3:
        num1, num2 = ask()
        print(multiply(num1,num2))
    elif choice == 4:
        num1, num2 = ask()
        print(devide(num1,num2))
    elif choice == 5:
        break
    else:
        print("Invalid Choice")