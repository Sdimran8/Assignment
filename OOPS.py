# Defining a class

# class Biryani:
#     def __init__(self,smell,taste,texture,meatContent,color):
#         self.smell = smell
#         self.taste = taste
#         self.texture = texture
#         self.meatContent = meatContent
#         self.color = color


# Hyderabadi = Biryani('onion','spicy','smooth',True,'yellow')
# Donne = Biryani('podina','moderate spicy','rough',True,'green')
# Avadi = Biryani('haldi','low spicy','sticky',False,'white')

# print(Donne.smell)

#Inheritance

# class Animal: #parent class

#     def eat(self):
#         return('I eat food')
#     def sleep(self):
#         return('I can sleep')
#     def see(self):
#         return('I can watch')

# class Dog(Animal): #child class
#     def bark():
#         return('I bark')
#     def run():
#         return('I can Run')

# d = Dog()
# print(d.sleep())            

# Polymorphism - utensils

# class PressureCooker:
#     def cook(self):
#         print('only food will cook in pressure')

# class Kadhai(PressureCooker):
#     def cook(self):
#         print('i am used for shallow frying')

# class Wok (PressureCooker):
#     def cook(self):
#         print('chinnese food')

# w = Wok()
# w.cook()

# k = Kadhai()
# k.cook()

# k = Kadhai()
# k.cook()


# class Sports:
#     def __init__(self,country,players,timings,matches,refree):
#         self.country = country
#         self.players = players
#         self.timings = timings
#         self.matches = matches
#         self.refree = refree

# cricket = Sports('India','11',5,3,4)
# Hockey = Sports('Australia','14',90,40,2)
# football = Sports('Brazil','12',100,70,5)

# print(cricket.players)
# print(football.matches)

# class movies :
#     def __init__(self,firm,latm,height,weight):
#         self.firm = firm
#         self.latm = latm
#         self.height = height
#         self.weight = weight

# prabhas = movies('Raghavendra','Salaar',6,80)
# mb = movies('Arjun','Gk',5.8,70)
# pk = movies('kushi','bro',5.5,65)

# print(mb.height)

# class Teacher:
#     def study(self):
#         return('can study')
#     def write(self):
#         return('can writes well')
#     def teach(self):
#         return('teaches well')

# class student(Teacher):
#     def perfoms(self):
#         return('I perfoms Well')
#     def exam(self):
#         return('Rank first')

# v =  student()
# print(v.exam()) 

# class Software:
#     def Jobs(self):
#         print('can do all softwares')
# class Accounts:    
#      def Jobs(Software):
#         print('can do all Taxes')
# class Sap:       
#      def Jobs(Software):
#         print('can do all modules')

# A = Accounts()
# A.Jobs()   

# s = Sap()
# s.Jobs()

#Encapsulation

# class BankAccount:
#     def __init__(self,accountNum,balance):
#         self.acNo = accountNum
#         self.__bal = balance #private variable
        
#     def withdraw(self,amt):
#         if amt > self.__bal:
#             return('In sufficient Balnce')
#         else:
#             self.__bal = self.__bal-amt

#     def deposit(self,amt):
#         if amt > 0:
#             self.__bal = self.__bal + amt
#             return self.__bal
#         else:
#             return("Invalid Amt")

#     def checkbal(self):
#         return self.__bal

# imranAc = BankAccount(987654321,1000008000)
# print(imranAc.checkbal())

# imranAc.withdraw(100000)
# print(imranAc.checkbal())

# imranAc.deposit(123456789)
# print(imranAc.checkbal())

#scope local & global variable

# n =20
# def fun():
#     a = 10
#     print(a)
# fun()    
# print(n)
