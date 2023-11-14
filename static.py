
# How to declare static variables Types:

# class student:
#     a = 100
# t = student()
# print(t.a)

#---------------------------------------#

# class student:
#     def __init__(self):
#         student.a = 20
#     def m1(self):
#         student.a = 21
# t = student()
# t.m1()
# print(t.a)        

#-------------------------------------------#

# class student:
#     a =80
#     def __init__(self):
#         student.b = 5
#     def m1(self):
#         student.c = 4
#     @classmethod
#     def m2(cls):
#         student.d = 21
#         cls.e = 98
#     @staticmethod
#     def m3():
#         student.f = 33

# f = student()
# student.m2() 
# print(student.__dict__)                 

#-------------------#
# from colorama import Fore

# print(Fore.YELLOW+"Hello world")
# print(Fore.RED+"Hello world")
# print(Fore.BLUE+"Hello world")
# print(Fore.BLACK+"Hello world")
# print(Fore.CYAN+"Hello world")
# print(Fore.GREEN+"Hello world")