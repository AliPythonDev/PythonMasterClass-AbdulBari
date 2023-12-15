#Q4) check if a number is a palindrome .
# if the reverse of a number is equal to the original number then we say its a palindrome
n = int(input("Enter a Number which you want to take Palindrome: "))
m = n
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
print("The Reverse of a Number is ", rev)
if m == rev:
    print("The Given Number is a Palindrome.")
else:
    print("The Given Number is not a Palindrome.")