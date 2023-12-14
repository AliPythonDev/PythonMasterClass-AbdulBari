#Q3) find the maximum numbers from the given number.
num_of_nos = int(input("Enter a Number which you want to find Max: "))
count = 0
max = int(input("Enter a Number: "))
while count < num_of_nos - 1:
    n = int(input("Enter a Number: "))
    if n > max:
        max = n
    count += 1

print("The Maximum Number is ", max)