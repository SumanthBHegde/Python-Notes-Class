#Checking if the given number is prime or not
def chek_prime(n):
    if n>1:
        for i in range(2,(n//2)):
            if n%i == 0:
                print(f"{n} is not prime")
                break
    else:
        print(f"{n} is prime")

#Input the number
num = int(input("Enter any  number: "))
chek_prime(num)
