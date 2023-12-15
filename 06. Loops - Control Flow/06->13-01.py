#Q1) Print n terms of A.P Series.
a = int(input("Enter a first term of an A.P: "))
d = int(input("Enter a common difference of an A.P: "))
n = int(input("Enter total number of terms in an A.P: "))
for t in range (a, a + n * d , d): # (5, 10, 2)
    print(t)
