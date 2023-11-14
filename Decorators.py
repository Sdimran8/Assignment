# def div(func): #division(10,5) #function and arguments passes in func
#     def inner(a,b):  #a=10,b=5 #it will be the input of div(func)
#         if b==0:  #5==0
#             print("cannot be divided")
#         else:
#             return func(a,b)  #division(a,b)
#     return inner

# @div
# def division(a,b):
#     return a/b

# print(division(10,5))
# print(division(10,0))

# def decor1(func):
#     def inner(name):
#         print("frist decor",name,"execution")
#         func(name)
#     return inner

# @decor2
# def message(name):
#     print("hello",name,"how are you")
#     message("aman")
# def decor2(func):
#     def inner (name):
#         print("second decor",name," execution")
#         func(name)
#     return inner 

# @decor1

# def decor1(func):#20
#     def inner():
#         x=func()
#         return x*x
#     return inner

# def decor2(func):#num (10)
#     def inner():
#         x=func()
#         return 2*x #20
#     return inner

# @decor1
# @decor2
# def num():
#     return 10
# print(num())


# import pyautogui
# import time
# time.sleep(8)
# count = 0
# while count<= 500:
#     pyautogui.typewrite("Hello")
#     pyautogui.press("enter")
#     count = count +1

# import pyautogui as p
# import time
# time.sleep(4)
# for i in range(10):
#     p.typewrite("Hello")
#     p.press("enter")

# import pyautogui
# print(pyautogui.__version__)

# def str_upper(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner
# @ str_upper  

# def print_str():
#     return "Good Morning"
# print(print_str())    

# def div_decor(func):
#     def inner(x,y):
#         if y == 0:
#             return "give proper input"
#         return func(x,y)
#     return inner
# @ div_decor
# def div(a,b):
#     return a/b

# print(div(4,0))
