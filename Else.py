# try:
#     print("try")
# except:
#     print("Except")
# else:
#     print("Else")
# finally:
#     print("Finally")

# print("Outside the block")            

#-------------------------------------------------------------------------------------------# 1,3,5,6

# try:
#     print("try") #stataement -1
#     print(10/0) #stataement -2
# except ZeroDivisionError:
#     print("Except") #stataement -3
# else:
#     print("Else")   #stataement -4
# finally:
#     print("Finally") #stataement -5

# print("Outside the block") #stataement -6    

#------------------------------------------------------------------------------------------# Exception not matched 1 & 5

# try:
#     print("try") #stataement -1
#     print(10/0) #stataement -2
# except TypeError:
#     print("Except") #stataement -3
# else:
#     print("Else")   #stataement -4
# finally:
#     print("Finally") #stataement -5

# print("Outside the block") #stataement -6    

#-------------------------------------------------------------------------------------------#1,2,3,5,6

# try:
#     print("try") #stataement -1
#     print("Hey") #stataement -2
# except ZeroDivisionError:
#     print(10/0) #stataement -3
# else:
#     print("Else")   #stataement -4
# finally:
#     print("Finally") #stataement -5

# print("Outside the block") #stataement -6    

#---------------------------------------------------------------------------------------------#

# try:
#     print("try") #stataement -1
#     print(10/0) #stataement -2
# except ZeroDivisionError:
#     print("INDIA")
#     print(10/0) #stataement -3
# else:
#     print("Else")   #stataement -4
# finally:
#     print("Finally") #stataement -5

# print("Outside the block") #stataement -6    

#------------------------------------------------------------------------------------------------# 1,2,5

# try:
#     print("try") #stataement -1
#     print("heyy") #stataement -2
# except ZeroDivisionError:
#     print("Except") #stataement -3
# else:
#     print(10/0)   #stataement -4
# finally:
#     print("Finally") #stataement -5

# print("Outside the block") #stataement -6    

#---------------------------------------------------------------------------------------------------# 1,2,4

# try:
#     print("try 1") #stataement -1
#     print("try 2") #stataement -2
# except ZeroDivisionError:
#     print("Except") #stataement -3
# else:
#     print("Else")   #stataement -4
# finally:
#     print(10/0) #stataement -5

# print("Outside the block") #stataement -6    

#-----------------------------------------------------------------------------------------------------#

# try:
#     print(10,-'a')
# except TypeError:
#     print("string")
# else:
#     print("Else Block")
# finally:
#     print('Finally')
# print('Outside block')

#-------------------------------------------------------#

# try:
#     try:
#         print(200**7777)
#     except ValueError:
#         print("Big value")
#     else:
#         print("el")
#     finally:
#         print("fo")        
# except:
#     print('except')        
# else:
#     print("e")
# finally:
#     print("f")
# print("out")        

# #------------------------------------------------#
# n = "ram"
# try:
#     if n == 'kumar':
#         print("hey")
#     else:
#         print("helo")    
# except:
#     print("Bro")
# else:
#     print("e")
# finally:
#     print("f")
# print("out")          

#----------------------------------------------------------#

# try:
#     print(10-"a")
#     try:
#         print("how")
#     except TypeError:
#         print("king")
#     finally:
#         print("fin")
# except TypeError:
#     print('koko')
# else:
#     print("hey")    
# finally:
#     print("O")    
# print('decc')                

#--------------------------------------------------------#     

# try:
#     print(10-0.99)
# except:
#     print('hello')
# else:
#     print("Bro")
# finally:
#     print('f')
# print('hi')                     

#----------------------------------#  

# try:
#     print(10/2098)
# except:
#     print('2.0')
# else:
#     print("Else")
# print('Hoh')        

#-----------------------------------------#

# try:
#     k = int(input('enter  '))
#     print(k)
# except ValueError:
#     print("Error Found")
# else:
#     print("e")
# finally:
#     print("fi")           

#-----------------------------------------#

# try:
#     print(10+"a")
# except TypeError:
#     print("hoe")
# else:
#     print("e")
# finally:
#     print("fi")      

#-----------------------------------------#

# try:
#     print(10+a)
# except NameError:
#     print("hoe")
# else:
#     print("e")
# finally:
#     print("fi") 

#------------------------------------------#
# import time
# try:
#     for i in range(1,100):
#         time.sleep(2)
#         print("HI",i)
#         i = i+1
# except KeyboardInterrupt:
#     print("stops")

# finally:
#     print('f')
# print('j')    

#------------------------------------------#

# try:
#      D1={'1':"aa", '2':"bb", '3':"cc"}
#      print(D1['4'])
# except KeyError:
#     print("not ")
# else:
#     print("Else")

#----------------------------------------------#

# try:
#     my_list = [i for i in range(1000000000)]
#     print(my_list)
# except MemoryError:
#     print("Error")
# else:
#     print("key")
# finally:("fin")    
#-----------------------------------------#

#1. Predefined Exceptions (inbuilt Exception) zero div Err
#2. User Defined Exceptions (It is customised Exception) (Every class is an Exception)

# class Eligible(Exception):
#     def __init__(self,a):
#         self.msg = a

# class NotEligible(Exception):
#     def __init__(self,a):
#         self.msg = a        

# age = int(input("Enter your age to check for your Eligibility : "))

# if age > 18:
#     raise Eligible("Your Eligible for voting")

# elif age<18:
#     raise NotEligible("Your not Eligible for Voting")
