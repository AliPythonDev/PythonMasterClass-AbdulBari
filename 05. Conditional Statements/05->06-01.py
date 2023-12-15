#Check if a student has Passed or Failed, by taking marks in 3 subjects.
math = int(input("Enter Marks in Mathematics Subject "))
phy = int(input("Enter Marks in Physics Subject "))
chem = int(input("Enter Marks in Chemistry Subject "))
if math>=45 and phy>=45 and chem>=45:
    print("Congratulations! You are Passed.")
else:
    print("Sorry you are Failed, Better Luck Next Time.")
