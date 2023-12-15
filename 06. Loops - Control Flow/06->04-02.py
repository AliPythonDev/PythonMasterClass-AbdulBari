#Q2) Finding sum of digits in a number
#If the number is given then find its sum by using while loop
n = int(input("Enter a Number which you want to take Sum: "))
sum = 0
counter = 0
while n > 0:
    r = n % 10
    n = n // 10
    counter += 1
    sum = sum + r
print("The Sum of ", counter, " digits are ", sum )

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

#sum = sum + r
# 0 = 0+9
# 14 = 9+5
# 17 = 14+3
# 19 = 17+2
# 20 = 19+1