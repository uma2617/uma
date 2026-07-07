product_price = 5000
delivery_charges = 100

total = product_price + delivery_charges
print(total)



###############
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

student = 10
groups = 2

print(student // groups)

################################

#followers = 100
#followers += 1
#print(followers)

################

saved_password = "10"
entered_password = "20"

print(saved_password == entered_password)
print(saved_password > entered_password)
print(saved_password < entered_password)
print(saved_password >= entered_password)
print(saved_password <= entered_password)
print(saved_password != entered_password)


################################################

balance = 1500
pin_correct = True
if balance >= 1000 and pin_correct:
    print("Withdraw allowed")
else:
    print("failed")


    #################

product = input("Enter product name:")
price = int(input("Enter product price:"))
quantity = int(input("Enter quantity:"))
total = price * quantity
discount = total * 0.10
final_bill = total - discount
print("Product =",product)
print("Total =",total)
print("Discount =",discount)
print("Final bill =",final_bill)