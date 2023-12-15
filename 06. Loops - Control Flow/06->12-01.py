#Q1) Display multiplication table for a given number.
n = int(input("Enter a Number which you want to Print a Table: "))
for count in range(1,11):
    print(count, " X ", n, " = ", n*count)
