#Q2) Find the sum of +ve and -ve number.
#User may enter positive or negative number.
num_of_nos = int(input("Enter a Number which you want to take Sum: "))
psum = 0
nsum = 0
count = 0
while count < num_of_nos:
    n = int(input("Enter a Number: "))
    if n > 0:
        psum = psum + n
    else:
        nsum = nsum + n
    count += 1
print("The Sum of Positive Numbers are ", psum)
print("The Sum of Negative Numbers are ", nsum)
