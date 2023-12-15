#Nested for loop with Strings
s1 = "abc"
s2 = "xyz"
for i in s1:
    for j in s2:
        print(i, j , end=" " )
    print("")
# Output:
# a x a y a z
# b x b y b z
# c x c y c z