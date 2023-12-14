#Q1) find sum of given numbers as input
#Ask number of numbers by taking user input and find the sum of that inputs And we have to count so we use counter for it.
num_of_nos = int(input("Enter a Number which you want to take Sum: "))
sum = 0
count = 0
while count < num_of_nos:
    n =  int(input("Enter a Number: "))
    sum = sum + n
    count += 1
print("The Sum of Total Numbers are: ", sum)