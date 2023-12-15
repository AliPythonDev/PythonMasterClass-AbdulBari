#Q1) Counting the number of digits in a number.
#Taking input from user in integrant write a counter condition in while loop for just counting the numbers given as input from user.
n = int(input("Enter a Number which you want to Count: "))
counter = 0
while n > 0:
    n = n // 10
    counter = counter + 1
print('The total digits are: ', counter)