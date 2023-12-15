#Star Patterns (P-a)
# for i in range(0 , 5):        #Rows
#     for j in range(0, 5):     #Columns
#         print("*" , end=" " )
#     print("")
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#Star Patterns (P-b)
# for i in range(0 , 5):
#     for j in range(0, 5):
#         if i <= j:
#             print("*" , end=" " )
#     print("")
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

#Star Patterns (P-c)
for i in range(0 , 5):
    for j in range(0, 5):
        if i >= j:
            print("*" , end=" " )
    print("")
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *