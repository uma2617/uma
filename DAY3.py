# # student = ("ram","sam","bheem")
# # print(student[-2])
# # numbers = (10,20,30,40)
# # print(numbers [-3])

# # data = (1,2,3)
# # data[0] = 100
# # print(data)

# # x = (1,2,3,2,1,1,4)
# # print(x.count(1))
# # print(x.count(2))

# # x = ("apple","banana","grapes","banana")
# # print(x.count("banana"))

# # num = (10,20,30,40,50)
# # print(num[1:4])

# # ######sets###
# # x = {1,2,3,1,1,1,4}
# # print(x)
# # data = {1,2,3}
# # data.add(4)
# # print(data)

# # a ={1,2,3}
# # b = {3,4,5}
# # print (a|b)

# # ##########functiton##########

# # def greeting():
# #     print("hello students")
# # greeting()

# def add():
#     return 10 + 20
# result=add()
# print(result)

# def mulitply():
#     return 10 * 20
# result=mulitply()
# print(result)

# def sub():
#     return 10 - 20
# result=sub()
# print(result)

# def add(a,b):
#     print(a+b)
# add(10,20)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def darling(*numbers):
#     print(numbers)
# darling(10,20,30,40,50,60)

# def add(*num):
#     total = 8
#     for i in num:
#         total += i
#     print(total)
# add(10,20,30,40,50,60)

# #########**kwargs**#########

# def student(**details):
#         print("name:",details["name"])
#         print("age:",details["age"])
#         print("job:",details["job"])
# student(
#         name="lucky",
#         age=22,
#         job="sales",
#     )

# def square(x):
#     return x * x
# print(square(16))
# square= lambda x:x*x
# print(square(25))

# add= lambda a,b:a+b
# print(add(10,20))

# multiply=lambda a,b:a*b
# print(multiply(10,20))

# even_odd = lambda x:"even" if x%2 else "odd"
# print(even_odd(10))
# print(even_odd(7))

# upper=lambda x : x.upper()
# print(upper("lucky"))

# lucky = lambda text:len(text)
# print(lucky("rukumini vasanth"))

# file = open("student.txt","w")
# file.write("hello lucky")
# file.close()

# print("data written successfully")
# file= open("student.txt","r")
# data=file.read()
# print(data)
# file.close()

# file=open("student.txt","a")
# file.write("\nhow are you")
# file.close()

# print("data append successfully")

# file=open("student.txt","r")
# print(file.read())
# file.close()

# try:
#     num =  int(input("enter number:"))
#     print(num)
# except valueError:
#     print("only number allowed")
# try:
#     a = int(input("enter A:"))
#     b = int(input("enter b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divided by zero")
# except ValueError:
#     print("enter onnly numbers")
# try:
#     file =open("data.txt")
#     print(file.read())
# except:
#     print("file error")
# finally:
#     print("program completed")

# try:
#     print(10/2)
# except:
#     print("error")
# else:
#     print("success")