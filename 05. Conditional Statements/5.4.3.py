#Check for Age Eligibility for Casting a Vote.
s = str(input("Enter your Name "))
n = int(input("Enter your Age "))
if n>=18:
    print("Congratulations!", s , "You are Eligible for Vote.")
else:
    print("Sorry" , s,", You are not Eligible for Vote.")