#Match case is used instead of switch case in languages like c++, java we use switch case it is like if else.
#It is similar to if else but syntax written is similar to switch case . But works same as if and elif.
# day = int(input("Enter a Number: "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Holiday")

#This Program is similar as:
# day = int(input("Enter a Number: "))
# if day == 1:
#         print("Monday")
# elif day == 2:
#         print("Tuesday")
# elif day == 3:
#         print("Wednesday")
# elif day == 4:
#         print("Thursday")
# elif day == 5:
#         print("Friday")
# elif day == 6:
#         print("Saturday")
# elif day == 7:
#         print("Sunday")
# else:
#         print("Holiday")

# This code will keep taking input numbers until you enter "exit" to quit the loop. If you enter a number, it will display the corresponding day or "Holiday." To exit the loop and stop entering numbers, simply type "exit."
while True:
    day = input("Enter a Number (or 'exit' to quit): ")

    if day.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered.

    day = int(day)  # Convert the input to an integer.

    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Holiday")
