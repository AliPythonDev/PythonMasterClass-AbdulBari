#Q2) Print n terms of Fibonacci Series.
n = int(input("Enter a Number which you want to find a Fibonacci: "))
a = 0
b = 1
for i in range (n): #If you think 0 is not the first term then you can simply do if  {for i in range (n+1):}
    print(a)
    c = a + b
    a = b
    b = c