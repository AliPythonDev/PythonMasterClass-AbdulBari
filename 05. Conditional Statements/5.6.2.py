#Check if a person is authorize for admin access.
username = input("Enter your Name ")
if username == 'john' or username == 'John' or username == 'smith' or username =='Smith':
    print("Access Granted.")
else:
    print("Access Denied.")