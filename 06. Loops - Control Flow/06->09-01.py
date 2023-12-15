#Infinite Loop and Brake Statements
#Part a)
# count = 0
# while count < 10:
#     print("Hey")

#This while loop never stops, you need to keep on giving input and it generated results it never stops
# while True:
#     n = int(input("Enter a Number: "))
#     if n > 0:
#         print("The Given Number is a Positive Number.")
#     else:
#         print("The Given Number is a Negative Number.")

#Part b)

#To stop such infinite loop we can use break statement
# • A break statement will stop the loop then and there
# • A break statement can be used in other loop situations as well apart from infinite loop
# • The below example shows the use of break statement
while True:
    n = int(input("Enter a Number: "))
    if n>0:
        print("The Given Number is a Positive Number.")
    elif n<0:
        print("The Given Number is a Negative Number.")
    else:
        break
# If you want to stop Loop without completion at some point then use Brake. It will end at 0.
#Break
# count = 0
# while count < 10:
#      print(count)
#      count = count + 1
#      if count > 5:
#          break