#Continue and Pass Statements
#Part a)
#Continue
# count = 0
# while count < 10:
#     n = int(input("Enter a Number: "))
#     if n % 3 == 0:
#         continue
#     print(n)
#     count += 1
#Continue means it will not execute the rest of the statements in the loop and simply go to the beginning of the loop so rest of the statements aren't executed.
#Continue is used for logical design

#Part b)
#Pass
#If a Number is Divisible by 3 then don't print that number.
count = 0
while count < 10:
    n = int(input("Enter a Number: "))
    if n % 3 == 0: #If Number is Divisible by 3 then Pass otherwise Print
        pass        #Pass means Do Nothing.
    else:
        print(n)
    count += 1
#If you don't have to do anything in some cases then you can use pass.
#In python when you write a block of code you must write something if there’s nothing to write , then simply write pass statement.

#Same thing can be written without using Pass but statement will be changed.
##If a Number is not Divisible by 3 then print that number.
# count = 0
# while count < 10:
#     n = int(input("Enter a Number: "))
#     if n % 3 != 0:
#         print(n)
#     count += 1
#The Places where you don't have to do anything but have to write some statements then use pass.