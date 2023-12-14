#Check whether a given year is a leap year or not.
year = int(input("Enter a Year "))
if year % 400 == 0 and year % 100 == 0:
    print("It's a Leap Year.")
elif year % 4 == 0 and year % 100 != 0:
    print("It's a Leap Year.")
else:
    print("It's not a Leap Year.")