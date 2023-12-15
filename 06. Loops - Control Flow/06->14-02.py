#Q2) Check if a given Number is Prime or not.
n = int(input("Enter a Number which you want to find out whether it is Prime or not: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("It is a Prime Number")
else:
    print("It is a not a Prime Number")