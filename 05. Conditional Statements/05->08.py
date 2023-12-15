#Challenge Discount Amount
amount = float(input("Enter your Amount "))
if amount<=1000:
    discount = amount * 10/100
elif amount>=1000 and amount<=5000:
    discount = amount * 20/100
elif amount>=5000 and amount<=10000:
    discount = amount * 30/100
else:
    discount = amount * 50/100
print("Your total discount is ", discount)
disamount = amount - discount
print("Your total amount is ", disamount)