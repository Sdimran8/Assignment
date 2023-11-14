# print(10/2)
# print(10/0) zero division error
# print(10/'zero')--- Type Error

# a = int(input('en'))
# print(a) #---- Value Error if we given in string

# import math
# num = int(input("Enter the input  "))
# try:
#     result = math.factorial(num)
#     print(result)

# except:
#     print("Please do not enter Negative Numbers")   

# try:
#     num = int(input("input :  "))
#     if num <=0:
#         raise NameError("please enter +ve num")
# except NameError as error:
#     print(error)            

# finally:
#     print("goodbye")


# def addNum(num1,num2):
#     try:
#         print(num1+num2)
#     except TypeError:
#         print("Please enter integer values")    
#     except NameError:
#         print('Incorrect Parameters')   
#     except Exception as e:
#         print(e)   

# (addNum(1,9))
# print("The End...")

# try:
#     print(10/0)
# except BaseException:
#     print("Aman")
# print("outside try & Except block")    

# try:
#     print(10/0)
# except ArithmeticError:
#     print("Aman")
# print("outside try & Except block")   

# try:
#     print(10/0)
# except NameError:
#     print("Aman")
# print("outside try & Except block")   

# try:
#     print(10/2) # statement -1
#     print(10/0) # statement -2   Abnormal Termnination
#     print(10/5) # statement -3

# except ZeroDivisionError:
#     print("heyy") # statement -4

# print("How are yuhh")  # statement -5  


# try:
#     print(10/2) # statement -1
#     print(10/0) # statement -2   Normal Termination
#     print(10/5) # statement -3

# except ZeroDivisionError:
#     print("heyy") # statement -4

# print("How are yuhh")  # statement -5  

# try:
#     print(10/2) # statement -1  
#     print(10/0) # statement -2 Abnormal Termination
#     print(10/5) # statement -3

# except ZeroDivisionError:
#     print(100/0) # statement -4

# print("How are yuhh")  # statement -5

# try:
#     print(round(10/2))
#     print(10/0)

# except ValueError:
#     print("Give correct value")

# except ZeroDivisionError:
#     print("Error Found")    

# try:
#     print(round(10/2))
#     print(10/'a')
#     print(10/0)
  

# except TypeError:
#     print("Give correct value")

# except ZeroDivisionError as k: # to know the error by Aliasing
#     print("Error Found",k)  

# print("heyy bruhh")

# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/'a')

# except TypeError:
#     print("Find Error")

# finally:
#     print("Print Anytime")    


# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/0)

# except ZeroDivisionError:
#     print("Find Error")

# finally:
#     print("Print Anytime")   


# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/3)

# except ValueError:
#     print("Find Error")

# finally:
#     print("Print Anytime")   

# print("Outside TRY-EXCEPT-BLOCK")    

# try:
#     print("SALAAR")
#     print(10/2)
#     print(10/3)

# except ValueError:
#     print("Find Error")

# finally:
#     print(10/0)   

# print("Outside TRY-EXCEPT-BLOCK") 

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("even")

# except:
#     print("Not an even number!")

#-------------------------------------------------------------------------------------------------------------------------------#
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# def zero(a,b):
#     try:
#         print(a/b)

#     except ZeroDivisionError:
#         print("Will not divided with Denominator O")

# zero(10,0)    

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# import math
# try:
#     math.sqrt(-100)
# except ValueError:
#     print('Positive number expected for square root operation')   

# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# def typerr(a,b):
#     try:
#         print(a/b)

#     except TypeError:
#         print("Please Enter a two numbers,but not string values")
        
# typerr("9",8)

# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

# def find_index(n,lst):
#     try:
#         print(lst[n])

#     except:
#         print("Index out of the range")    

# n = int(input('Enter index number '))
# lst = ["Python","React JS","Aws"]
# find_index(n,lst)

#  Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

# import time

# try:
#     num = 10

#     for i in range(1,1000):
#         time.sleep(1)
#         print("Hi " + str(num))
#         num = num +1

# except KeyboardInterrupt: # ctrl + c
#     print("Stoped By Using Ctrl + c")

# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

# try:
#     j = 5.0

#     for i in range(1, 1000):
#         j = j**i
#         print(j)

# except OverflowError:
#     print("Result is too large")        


# import math
# try:
#     print('Control off:', math.exp(700))
#     print('Control on:', math.exp(1000))
# except Exception as e:
#     print (e)

#---------------------------------------#
# To read the file and have to create the file

# f = open("syed.txt","r")
# print(f.read())   # print all lines
# print(f.readline(),end="") # print first line
# print(f.readline()) # print second line
# print(f.readline(8)) # It will print 8 chracters in first line

#------------------------------------------#

# To create the file, If it was not created

# f1 = open("abc","w")
# f1.write("Hello world") # it will not print in output, It will write in abc file
# f1.write("HYD") # if you remove and write it we will lost the data

#--------------------------------------------------------------#
# To append the file to existing file that was gone to last 

# f1 = open("abc",'a')
# f1.write("vja")

# f1 = open("abc","a")
# f1.write("INDIA")

#---------------------------#

# To copy the data from one file to other file by using for loop

# f = open("syed.txt","r")
# f1 = open("abc","w")

# for i in f:
#     f1.write(i)

#-----------------------------#
# class Eligible(Exception):
#     def __init__(self,a):
#         self.msg=a

# class NotEligible(Exception):
#     def __init__(self,a):
#         self.msg=a
    
# age=int(input("enter you are age to check vote eligibility : "))
# if age>18:
#     raise Eligible(" you are eligible for voting")
# elif age<18:
#     raise NotEligible(" you are not eligible need to get 18 years for voting")

#---------------------------------------------------------------------------------------------------#

# f = open("abhi.txt","w")
# print(f)


