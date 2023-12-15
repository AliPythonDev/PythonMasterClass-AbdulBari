#Write a program to print output of the given number from last to first.
# Take input from users in integer form , the condition should be a number greater than zero and divide the number and print its result in integer form only.
n = int(input("Enter a Number: "))
while n>0:
    r = n % 10
    n = n // 10
    print(r)

# r = n % 10
# => 1245 % 10 = 5
# => 124 % 10 = 4
# => 12 % 10 = 2
# => 1 % 10 = 1

# n = n // 10
# => 1245 // 10 = 124
# => 124 // 10 = 12
# => 12 // 10 = 1
# => 1 // 10 = 0
