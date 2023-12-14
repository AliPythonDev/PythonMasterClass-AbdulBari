#else suite else with while loop
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
# else:
#         print("Print all 10 Numbers.")
# print("End of the Program.")
#This will print all the numbers with else statement.
#This else block will execute only if loop has stopped by becoming false, condition became false, then only else block.
#It's just like if else, if condition is true while loop will execute and if false else block will execute. If while never became false then else block will never execute
#So else block is used to confirm that while loop has successfully executed without any break in the middle
#• The else suite will be always executed irrespective of the statements in the loop are executed or not.
count = 1
while count <= 10:
    print(count)
    count += 1
    if count > 5:
        break
else:
        print("Print all 10 Numbers.")
print("End of the Program.")
#This will print all the numbers <6 and would not execute else statement because we used Brake statement.
# so, else block is used to confirm that while loop has executed successfully. and it stops when it becomes false.
# • If it stops abruptly using break then else will not execute.
