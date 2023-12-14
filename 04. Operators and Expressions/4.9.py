import math
a = float(input("Enter Value of A "))
b = float(input("Enter Value of B "))
c = float(input("Enter Value of C "))
x1= (- b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (- b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print("Roots are ",x1, x2)