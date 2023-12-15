#Q2) Find the factorial of a given number.
n = int(input("Enter a Number which you want to find a Factorial: "))
fact = 1
for count in range(1 , n+1):
    fact = fact * count
print("The Factorial of", n , " is ", fact)