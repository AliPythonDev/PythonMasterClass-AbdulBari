#Q4) Convert Decimal to Binary.
n = int(input("Enter a Number which you want to find Binary: "))
m = n
bin = 0
while n > 0:
    r = n % 2
    n = n // 2
    bin = bin * 10 + r
#The answer will be in Reversed form.
brew = 0
while bin > 0:
    r = bin % 10
    bin = bin // 10
    brew = brew * 10 + r
#It will reverse the Number.
print("The Binary of ", m , " is ", brew)

