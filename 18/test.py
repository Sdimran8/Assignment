# f = open("abhi.txt","w")
# # print(f)
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.readable())
# print(f.writable())

# f = open("Marolix.txt",'w')
# f.write("SAlaar ")
# f.write("Is a ")
# f.write("Hit Movie ")
# list1 = ["Baahubali ","is ","a ","hit ","movie "]
# f.writelines(list1)


# f = open("Marolix.txt",'r')
# d=f.read(10)
# print(d)

# f = open('Marolix.txt','r')
# print(f.readlines(100))

# f = open('Marolix.txt','r')
# print(f.readline(100))


# file = open("myfile.txt",'w')

# students = ['ram','sai','imran','chinnu','indu']
# marks = [85,90,75,70,95]
# htnumber = [123,234,456,567,678]

# for i in range(0,5):
#    entry = students[i] + "-" + str(marks[i])+'\n'
#    file.write(entry)
#    entry = students[i] + "-" + str(htnumber[i])+'\n'
#    file.write(entry)
    
# file.close()

# list_roll = ['1 ','2 ','3 ','4 ','5 ']
# f.writelines(list_roll)
# list_name = ['imr ','str ','int ','flo ','bool ']
# f.writelines(list_name)

#--------------------------------------------------------------#

# num = int(input("enter the no of students "))
# f = open("student.txt",'w')
# for i in range(num):
#     print("Enter details of the students",i+1,"students")
#     roll = int(input('Enter roll no '))
#     name = input("enter the name ")
#     marks = int(input('enter marks '))
#     details = str(roll) + "," + name + "," + str(marks) + "\n"
#     f.write(details)

#-----------------------------------------------------------#

# f = open("Marolix.txt",'r')
# print(f.tell())
# print(f.read(6))
# print(f.tell())
# f.seek(16)
# print(f.tell())

#--------------------------------------------------------#

# f = open('Marolix.txt','r')
# print(f.tell())
# print(f.read(8))
# print(f.tell())
# print(f.read(8))
# print(f.seek(8))

#---------------------------#
# To check the file is available or not.

# import os

# f = os.path.isfile('Marolix.txt')
# print(f)

#--------------------------------------#

#copying the image

# a1 = open('prb.jpg','rb')
# a2 = open('newprb.jpg','wb')
# b = a1.read()
# a2.write(b)

#--------------------------------#

#count the num of lines,chars,words

# f = open("count.txt",'r')
# num_of_words = 0
# num_of_lines = 0
# num_of_chars = 0

# for line in f:
#     num_of_lines +=1
#     line = line.strip("\n")
#     num_of_chars += len(line)
#     list_1 = line.split()
#     num_of_words += len(list_1)

# f.close()

# print(num_of_chars)
# print(num_of_lines)
# print(num_of_words)   

#---------------------------------------------#

# write a program to show the content of a file and if file not exist then tell the user file is not available

# import os
# filename = input("Enter the file name ")
# if os.path.isfile(filename):
#     f = open(filename)
# else:
#     print("File not Found")     

#------------------------------------#
# video

# f1 = open('video.MP4','rb')
# f2 = open('water.MP4','wb')

# f3 = f1.read()
# f2.write(f3)
#------------------------------------------#


# import csv
# with open("student.csv",'w') as f:
#     w = csv.writer(f)
#     w.writerow(['STU_name','STU_roll',"STU_father","STU_father_num","STU_Add"])
#     n = int(input("Enter the num of students : "))
#     for i in range(n):
#         Sname = input("Enter the student name : ")
#         Sroll = int(input("ENter the student rollno : "))
#         Sfath = input("Enter the student father name : ")
#         Sfathno = int(input("ENter the student father num : "))
#         w.writerow([Sname,Sroll,Sfath,Sfathno])

# print(n,"student data is saved succesfully")        

# import csv

# f = open("student.csv",'r')
# a = csv.reader(f)
# print(list(a))

# a = "Imran is a good boi"
# b = a.split()
# c = b[::-1]
# d= ' '.join(c)
# print(d)

# for i in b[::-1]:
#     print(i,end=' ')

# import csv

# f = open('student.csv','r')
# d = csv.reader(f)
# a = list(d)
# for i in a:
#     for j in i :
#         print(j,"\t",end=' ')
#     print()    

#----------------------------------------------#
# To know which current folder we open

# import os 
# a = os.getcwd()
# print(a)

# How to create the new Folder

# import os

# a = os.mkdir("Old")
# print("Created dir")

# to create sub folder
# a = os.mkdir('old/gold')

#--------------------------------------#

# class Stu:
#     def __init__(self,stid,stname,stadd):
#         self.stid = stid
#         self.stname = stname
#         self.stadd = stadd

# a = Stu(123,"Imran","Vja")
# print(a.stadd)        

# import os
# os.getcwd()

# s = 'our product is best in the market'
# b = s.split()
# for i in b[::-1]:   
#     print(i,end= ' ')