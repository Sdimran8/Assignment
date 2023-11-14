# doc string

# class EmployeeName:
#     '''Always first letter should be capital'''

#     def __init__(self):
#         pass

# print(EmployeeName.__doc__)    

# help(EmployeeName)

#--------------------------------------#

# class Employee:
#     def __init__(self):
#         self.name = "aman"
#         self.id = 456
#         self.add = "Hyd"

#     def say(self):
#         print("Hi",self.name)
#         print("My id is",self.id)
#         print("My add is",self.add)    

# e = Employee()
# print(e.add) To print only one 
# e.say() To print everthing in that method

#---------------------------------------------------#

# class Emp:
#     def __init__(self,x,y,z):
#         self.name = x
#         self.id = y
#         self.add = z

#     def say(self):
#         print("Hi",self.name)
#         print("My id is",self.id)
#         print("My add is",self.add)     


# e1 = Emp('ram',23,'vij')
# print(e1.name)
# e1.say()

#--------------------------------------#

# class Employee:
#     def __init__(self,name,phn,add):
#         self.name = name
#         self.phn = phn
#         self.add = add

#     def display(self):
#         print(self.name)
#         print(self.phn)    
#         print(self.add) 

# e1 = Employee('imran',222,'vij')
# e2 = Employee('ram',111,'vsk') 
# print(e2.name) #display only one value      
# e1.display()  #display all value

#-------------------------------------------------#

# class Mobile:
#     def __init__(self,name,storage,price,camera):
#         self.name = name
#         self.storage = storage
#         self.price = price
#         self.camera = camera

#     def specs(self):
#         print(self.name)   
#         print(self.storage)   
#         print(self.price)   
#         print(self.camera)    

# specifications = [Mobile('iphone',128,60000,"8MP"),Mobile('Samsung',128,30000,'16MP')]

# for i in specifications:
#     i.specs() # prints everything in loop minimize code for writing 1000 lines of code

#------------------------------------------------------------------------------------#
# To print the constructor in the dict form

# class Emp:
#     def __init__(self):
#         self.name ='Chotu'
#         self.num = 88
#         self.add ='vij'    

# e = Emp()
# print(e.__dict__)


# class Emp:
#     def __init__(self):
#         self.a = 10
#     def m1(self):
#         self.b = 20

# e = Emp()
# print(e.__dict__)
# e.m1()
# print(e.__dict__)
# e.d = 40
# print(e.__dict__)


#---------------------------------------------#

# class Emplo:
#     def __init__(self):
#         self.a =1
#     def m1(self):
#         self.b = 2

# e1= Emplo() 
# e2 = Emplo()
# e1.m1()          
# e2.r = 200
# e1.o=700

# print(e1.__dict__)
# print(e2.__dict__)


#----------------------------------------------------------#
# class car:
#     def __init__(self):
#         print(id(self)) # automatic self id will print

# c = car()
# d = car()
# print(id(c))
# print(id(d))

#----------------------------------------------------------#

# Method without constructor

# class Amazon:
#     def __init__(self,name,modelno,price):
#         self.name = name
#         self.modelno = modelno
#         self.price = price

# a=Amazon("Tupperwear",4734,500)
# print(a.__dict__)   


# class Amazon:
#     def plastic(self,name,modelno,price):
#         self.name = name
#         self.modelno = modelno
#         self.price = price

# a=Amazon()
# a.plastic("Tupperwear",4734,500)
# print(a.__dict__)   

#-------------------------#

# class Test:
#     def __init__(self):
#         self.a =19
#     def m1(self):
#         self.b = 90
#     def m2(self):
#         self.d = 70

# t1 = Test()
# t1.c = 100
# t1.m1()
# t2 = Test()
# t2.m2()
# t2.d = 80
# t3 = Test()
# t3.j = 33
# t3.a = 80
# print(t1.__dict__)
# print(t2.__dict__)
# print(t3.__dict__)                

#-----------------------------------------------------#

# class Tes:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         print(self.a)
#     def sd(self):
#         print(self.b)

# t = Tes()
# print(t.a)
# t.sd()

#-----------------------------------------------#

#Static var:

class Employee:
    a=11
    def __init__(self):
        self.b = 40

e1 = Employee()       
e1.b = 22
e1.c =90
Employee.a =67

e2 = Employee()
print(e1.a,e1.b,e1.c)
print(e2.a,e2.b)

#--------------------------#

# x = 10

# def add():
#     x =3
#     x = x+3
#     print(x)

# x=1
# print(x)
# add()

