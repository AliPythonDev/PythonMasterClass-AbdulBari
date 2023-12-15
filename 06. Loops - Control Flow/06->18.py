#Print Prime Number from 1-100
#For finding numbers like if a number is given you have to do the count the factors of a number you have to make counts count=0. Then for i in range (1, n). From 1 to n itself we have write (n+1) .Here condition if n%1==0.
#• Giving value zero so we have to increment to check whether a no. is prime or not we have to count the factors and find the number of factors.
# • Outside of this for loop we have to write if count==2:
# • Then we have to print that .Because , it’s a prime number.
# • Otherwise doesn’t need to print it.
for n in range(1, 100+1):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(i)
