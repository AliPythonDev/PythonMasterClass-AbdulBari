#Check if a person is eligible to work. Working age ranges from 18-60 Years.
age = int(input("Enter your Age "))
if age>=18 and age<=60:
    print("Congratulations! You are Eligible to work with us.")
else:
    print("Sorry, You are not Eligible to work with us.")