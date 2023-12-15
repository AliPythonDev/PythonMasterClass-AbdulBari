#Q1) Find the factors of a Number.
n = int(input("Enter a Number which you want to find a Factor: "))
for i in range(1 , n+1):
    if n % i == 0:
        print("Factor of",n, "are" ,i)
