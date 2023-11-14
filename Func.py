# def f1():
#     print('Good mrng')
#     print('Good night')

# f1()
# f1()
# f1()
# f1()    

# def f1(a,b):
#     print(a+b)
#     print(a-b)
#     print(a/b)
#     print(a*b)

# f1(2,4)

#--------------------------------------------#

# 1.position Argument

# def f1(a,b):
#     print(a,"movie ki podama",b)

# f1("hey","eroju")    

# def f1(a,b):
#     print(a+b)

# f1(2,3)    

# 2.keyword Argument

# def f1(a,b):
#     print("hey",a,"how are you",b)


# f1("google",'man')
# f1(a='2',b='ok')
# f1('immu',b='fine')
# f1(b='immu',a='m')

# 3. Default Argument

# def f1(a='aman'):
#     print('hey',a,'wt dng')

# f1()
# f1('man')
# f1(a='imran')

# def fun():
#     print('hello')

# fun()

# def n(a='hi'):
#     return(a)

# print(n())

# def printnum(a,b):
#     print(a,b)

# printnum(1,2)    

# def pkd(a='hi',b=2):
#     print(a,b)

# pkd(8,7,a=10,b=99) #Invalid : got multiple values for argument 'a' 

# def a(a,b):
#     print(a,b)

# a(b='hi',"Hello") #Invalid : positional argument follows keyword argument

# def sd(a=20):
#     print(a)
# sd(10)    #Valid :it takes keyword arg first

# def fn(*para):
#     count = 0
#     for i in para:
#         count = count + i
#     print(count)    

# fn(2,3,8,17,9,4,2,3)

# def fn(*para,a):
#     print(a,para)    

# fn(2,3,8,1,9,4,a='aman')

#--------------------------------------------------------------------#
# write a func which contains some number as arguments and print square of that number     

# def sqr(a=7):
#     print(a*a)

# sqr()    

# write a program in multi given number is even or odd.

# def evod(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd") 
# evod(18) 

# write a func to find factorial of given number.

# def fact(a):
#     facto = 1
#     for i in range(1,a+ 1):
#        facto = facto*i
#     print(facto)          

# fact(3)

# write a program to create calculator using multis (sum,sub,mul,div)

# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def multi(a,b):
#     return(a*b)
# def div(a,b):
#     return(a/b)                

# print(add(3,2))
# print(sub(3,2))
# print(multi(3,2))
# print(div(3,2))

# write a pro to print sum of given numbers.

# def sumof(a=6,b=2):
#     count = 0
#     for i in (a,b):
#         count = count + i
#     print(count)
# sumof()        

#  write a program to enter student deatials and also view the stored student details 

# class Student:
#     marks = []
#     def getData(self,rn,name,m1,m2,m3):
#         Student.rn = rn
#         Student.name = name
#         Student.marks.append(m1)
#         Student.marks.append(m2)
#         Student.marks.append(m3)

#     def displayData(self):    
#         print("Roll Num is:",Student.rn)
#         print("Student name",Student.name)
#         print("marks in subject 1:",Student.marks[0])
#         print("marks are:",Student.marks)

#     def total(self):
#         return (Student.marks[0]+Student.marks[1]+Student.marks[2])    


# r = int(input("enter the roll num "))
# name = input("enter the num ")
# m1 = int(input('m1 '))
# m2 = int(input('m2 '))
# m3 = int(input('m3 '))

# s1 = Student()
# s1.getData(r,name,m1,m2,m3)
# s1.displayData()
# print('Total marks',s1.total())

# def length(stri):
#     return len(stri)

# print('Length of string',length("multi"))    

# def square( item_list ):        
#     squares = [ ]    
#     for l in item_list:    
#         squares.append( l**2 )    
#     return squares    
  
# my_list = [17, 52, 8];    
# my_result = square( my_list )    
# print( "Squares of the list are: ", my_result ) 


'local variable'
'global variable'

# n=30
# def sqr(a):
#     n=10
#     print(a*a)

# sqr(n)    

#------------------------------------------------------------------------------------#

# a = 10

# def f1():
#     print(a)

# def f2():
#     print(a)    

# f1()
# f2()

# a = 10

# def f1():
#     a = 50
#     global b
#     b = 40
#     print(a)

# def f2():
#     b = 11
#     print(b)    

# f1()
# f2()

# def f1():
#     global a
#     a=1
#     a=2
#     print(a)
# f1()    

# Recursion:

# def fact(a):
#     if a==0:
#         r=1
#     else:
#         r=a*fact(a-1)
#         return r    
# fact(4)

# w=(list(filter(lambda x:x%2==0,range(1,11))))
# print(w)

#Filter Func :

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)
# print(list(adults))

#2.
# def check_even(number):
#     if number % 2 == 0:
#           return True  

#     return False

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers_iterator = filter(check_even, numbers)
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)

#3.
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# def filter_vowels(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vowels else False

# filtered_vowels = filter(filter_vowels, letters)
# vowels = tuple(filtered_vowels)
# print(vowels)

#4.
# numbers = [1, 2, 3, 4, 5, 6, 7]
# even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)

#5.
# def filterdata(x):    
#     if x>5:    
#         return x        
# result = filter(filterdata,(1,2,6,88,9))        
# print(list(result))  

#Reduce :

# from functools import reduce    
# def add(a, b):  
#     return a + b  
  
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
# su = reduce(add, num_list)  
# print(su)  
    

# from functools import reduce   
# my_list = [1, 2, 3, 4, 5]   
# product = reduce(lambda x, y: x * y, my_list)  
# print(product) 

# from functools import reduce
# def is_true(a, b):
#    return bool(a and b)

# print(reduce(is_true, [1, 1, 1, 1, 1]))

# print(reduce(is_true, [1, 1, 1, 1, 0]))

#map---- iterable one at a time result is returned

# ans = map(lambda a: 2*a, [3, 5])
# print(list(ans))

# numbers = [2, 4, 6, 8, 10]

# def square(number):
#   return number * number
# squared_numbers_iterator = map(square, numbers)
# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)

# numbers = (1, 2, 3, 4)
# result = map(lambda x: x*x, numbers)
# print(result)

# numbersSquare = set(result)
# print(numbersSquare)

# recursive Func:

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 3
# print("The factorial of", num, "is", factorial(num)) 

# def factorial(n):  
#         if n==0:  
#             return 1  
#         else:  
#             return n*factorial(n-1)  
  
# num = 5 
# print("The factorial of a {0} is: ".format(num), factorial(num))  

#-------------------------------------------------------------------#

# def a(f):
#     print("hey bro",f)

# c=a
# a('ramu')
# c('aman')

# del a
# #a('goverdan')
# c('nihar')

# def f1():
#     print('first func')
#     def f2():
#         print("second func")
#     f2()
# f1()        

# def le(st):
#     print(len(st))

# le("multi")

# def my_multi(fname):
#   print(fname + " iphone")

# my_multi("Lumos")
# my_multi("Knox")
# my_multi("siri")

# def my_multi(*kids):
#   print("The youngest child is " + kids[0])

# my_multi("Gill", "Kohli", "Sachin")

# def funcall(*kw):
#     print("Num"+str(kw))

# funcall(1,2,3,4,5)    

# def dontknowkw(**arg):
#     print(arg)

# dontknowkw(a=1,b=2,c=3,d=4,e=5)

# def passinglist(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# passinglist(fruits)

# def multi(x):
#   return 5 * x

# print(multi(3))
# print(multi(5))
# print(multi(9))

# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ",sum)

# add_numbers(5, 4)    

# add = lambda num: num + 4    
# print( add(6) )    

# v = lambda k : k+str('bro18')
# print(v('HI my name is imran'))

# def a():
#     print("this is a func")
#     def inner():
#         print("this is inner function")
#     print("this is print statment A inside the inner function")
#     def inner1():
#         print("this is inner one function")
#     return inner1

# f=a()
# f()


# def a():
#     print("this is a func")
#     def inner():
#         print("this is inner function")
#     print("this is print statment A inside the inner function")
#     def inner1():
#         print("this is inner one function")
        
#     return inner1,inner

# f=a()
# f()


# def dec(f):#f(musthaq)
#     def inner(n):
#         if n=="goverdhan":
#             print("hi how are u")
#         else:
#             f(n)
#     return inner
# @dec
# def b(n):
#     print("hello")

# b("musthaq")
# b("goverdhan")
# b("aman")

