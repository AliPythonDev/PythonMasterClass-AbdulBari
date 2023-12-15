#Nested Loops
# The outer loop can contain any amount of inner loop
#• In each iteration of the outer loop inner loop execute all its iteration. For each iteration of an outer loop the inner loop re-start and completes its execution before the outer loop can continue to its next iteration.
for i in range(0 , 5):
    for j in range(0, 5):
        print("(", i , j, ")" , end=" " ) #To get output in a single line. #At the end of the line give a single space.
    print("") #It is moving to the Next line. (To give new line after an iteration.) Now it is behaving like a Matrix.
