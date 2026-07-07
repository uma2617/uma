product_charges = 1000
# delivery_charges = 200
# total = product_charges + delivery_charges
# print(total)

# #operators
# a = 3
# b = 9

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# student = 10
# groups = 2

# print (student // groups)


# followers = 100
# followers = followers + 1
# print(followers)

# saved_password = "1234abcd"
# entered_password = "1234abcd"

# print(saved_password == entered_password)

# balance = 2000
# pin_correct = True
# if balance >= 1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Power:", num1 ** num2)

# #conditional statements
# password = input("enter the password: ")
# if password == "admin123":
#     print("welcome")
# else:
#     print("invalid password")

# age = 20
# if age >= 18:
#     print("eligible to vote")


# marks = int(input("enter your marks:"))
# if marks >= 90:
#     print("9 CGPA")
# elif marks >=80:
#     print("8 CGPA")
# elif marks >=50:
#     print("7 CGPA")
# else:
#     print("fail")

# age = 25
# salary = 50000
# if age > 18 and salary > 30000:
#     print("loan approved")

# day = "sunday" 
# if day == "saturday" or day == "sunday":
#         print("holiday")

# username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Login Failed")

correct_pin = 1234
balance = 5000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("PIN Verified")

    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Wrong PIN")

####################################

for i in range(2,6):
    print(i)

users=["babu","ravi","arun"]
for users in users:
    print("message sent to", users)


for i in range(10):
    if i == 5:
        continue
    print(i)

password = ""
while password != "1234":
    password = input("enter password:")
    print("login success")