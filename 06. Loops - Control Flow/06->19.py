#Challenge Draw Patterns
#Star Patterns (P-a)
# for i in range(0 , 5):        #Rows
#     for j in range(0, 5):     #Columns
#         print("*" , end=" " )
#     print("")

#Another way of Printing this Pattern.
# for i in range(0 , 5):
#     print("* " * 5)

#Same Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#Star Patterns (P-b)
# for i in range(0 , 5):
#     for j in range(0, 5):
#         if i >= j:
#             print("*" , end=" " )
#     print("")

#Another way of Printing this Pattern.
# for i in range(0 , 5):
#     print("* " * (i+1))
#Or
# for i in range(1 , 6):
#     print("* " * i)

#Same Output:
# *
# * *
# * * *
# * * * *
# * * * * *

#Star Patterns (P-c)
# for i in range(0 , 5):
#     for j in range(0, 5):
#         if i <== j:
#             print("*" , end=" " )
#     print("")

#Another way of Printing this Pattern.
for i in range(5 , 0, -1):
    print("* " * i)
#Same Output:
# * * * * *
# * * * *
# * * *
# * *
# *