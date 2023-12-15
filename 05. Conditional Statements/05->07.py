#Nested if and Elif Statements.
ajay = float(input("Enter Ajay's Age "))
john = float(input("Enter John's Age "))
smith = float(input("Enter Smith's Age "))
if ajay>john and ajay>smith:
    print("Ajay is Eldest.")
elif john>smith:
    print("John is Edlest.")
else:
    print("Smith is Edlest.")