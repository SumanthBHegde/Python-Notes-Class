#Solving Quadratic equations using cmath
import cmath

a = float(input("Enter value a : "))
b = float(input("Enter value b : "))
c = float(input("Enter value c : "))

#Calculating using the quadratic formula
d = (b**2) - 4*a*c

sol1 = (-b - cmath.sqrt(d))/ (2*a)
sol2 = (-b + cmath.sqrt(d))/ (2*a)

print(f"The solutions are {sol1} and {sol2}")