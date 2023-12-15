#Q) Display multiplication table for a given number
#We have a number and for that we have to print a multiplication table, as the pattern for multiplying is same we are using while loop here.
n = int(input("Enter a Number which you want to print a Table: "))
counter = 1
while counter <= 10:
    print(counter, " X ", n, " = ", counter * n)
    counter += 1
