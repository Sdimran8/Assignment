# n = 'America'
# count = 0
# for i in n:
#     if i in 'aeiouAEIOU':
#         count = count + 1
#         print(i)
# print(count)       

# n = 'imran'
# o=[i for i in n if i in 'aeiouAEIOU']
# print(o)  

# l =['AMAN','toNny',"RaJu"]
# l2 = []
# l2.extend('AMAN')
# print(l2)

# t =(1,2,3)
# print(t)
# print(type(t))

# t1 =(1,2)
# t2 =(3,4)
# t3 = (t1*t2)
# print(t1+t2)
# print(t3)

# l=[1,2,3]
# l=tuple(l)
# print(l)

# t1 = (1,5,2,6,4,9)
# print(sorted(t1)) 

# t1=(1,2,3)
# t1[1] = 7
# print(t1)

# t1 = (1,2,3,4,5)
# print(t1.index(5))

# sum and Average of tuple

# t = (1,3,5,6,8,3,4,5,1)
# c = len(t)
# s = sum(t)
# a = s/c
# print(s)
# print(a)

#Write a program to display all prime numbers within a range.

# start = int(input('start '))
# end = int(input('end '))
# for i in range(start,end+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

#  Display Fibonacci series up to 10 terms.

# n = int(input('enter num'))  
# x = 0
# y = 1
# z = 0
# while z <= n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# Find the factorial of a given number.

# n = int(input("enter num"))
# factorial = 1
# if n>=1:
#     for i in range (1,n+1):
#         factorial = factorial *i
# print ("Factorial of the given number is:", factorial)

# Reverse a given integer number.

# num = int(input('enter num '))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num%10 
# #rev = 0 & %takes last value remainder
#     num = num//10 #same conditon
# print(rev)  

#Use a loop to display elements from a given list present at odd index positions.

# my_list = [1,4,2,7,5,8]
# for i in range(1,len(my_list)):
#     if i % 2 != 0:
#         print(my_list[i])

#Calculate the cube of all numbers from 1 to a given number.

# for i in range(1,20):
#     print(i**3)

#Find the sum of the series upto n terms.

#num = int(input('enter num '))
# su = 0
# for i in range(1,num+1):
#     su = su+i
#     i = i+1
# print(su) 

#Append new string in the middle of a given string.

# s1 = input('enter string ')
# s2 = input('middle string ')
# l = int(len(s1)/2+1)
# output = s1[:l]+s2+s1[l:]
# print(output)

# t = int(input("enter "))
# sum = 0
# for i in range(1,t+1):
#     sum = sum + i
# print(sum)
# avg = sum/i
# print(avg)    

# a=[3,4,1,6,9,20]
# print(sorted(a))
# print(sorted(a,reverse=True))
# a.sort()
# print(a)
# ggmembership
# a=(2,3,5,7,8)
# b= 2 in a
# print(b)

# j = 2,3,4,5,6
# k = 3 not in j
# print(k)

#packing & Unpacking
a = 1,2,3,4
e=1
b=2
c=3
d=4
print(e)
print(b)
print(c)
print(d)




