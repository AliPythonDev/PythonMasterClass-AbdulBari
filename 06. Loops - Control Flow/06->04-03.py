#Q3) Reversing a string
#Take input from user and make that given number into reverse order using while loop
n = int(input("Enter a Number which you want to take Reverse: "))
rev = 0
while n > 0:
    r = n % 10
    n = n//10
    rev = rev * 10 + r
print("The Reverse Number of the given Number is: ", rev)


# Explanation:
# Remainder -> r = n % 10
# 12359%10 -> 9
# 1235%10 -> 5
# 123%10 -> 3
# 12%10 -> 2
# 1%10 -> 1

# n = n // 10
# 12359//10 -> 1235
# 1235//10 -> 123
# 123//10 -> 12
# 12//10 -> 1
# 1//10 -> 0

#rev = rev * 10 + r
# 9 = 0 * 10 + 9
# 95 = 9 * 10 + 5
# 953 = 95 * 10 + 3
# 9532 = 953 * 10 + 2
# 95321 = 9532 * 10 + 1