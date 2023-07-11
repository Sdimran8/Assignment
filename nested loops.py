# # num1 = 40
# # num2 = 60
# # sum = num1+num2
# # print(sum)

# name =""
# while name!= "aman":
#     name=input("enter your name")
# print("correctly enter")    

# name =""
# password=""
# while name!="raju" and password!="1234":
#     name=input("enter user name")
#     password=input("enter your password")
# print("hello",name,"thank you",password)    

# print("hello""bye")

# s ="sunny"
# for i in s:
#     print(i,end='')

# s="sunny"
# count=0
# for i in s:
#     count=count+1
#     print(i)

# for i in range(1,10+1):
#     print(i)

# for i in range(21):
#     if i%2==0:
#         print(i)

# for i in range(4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j))

# n = int(input("Enter your input"))

# for num in range(n):
#     print('* ' *num)

# n = int(input("enter your input"))

# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==j:
#             print('*',end=' ')
#         else:
#             print(end=' ')    
#     print()   

# n = int(input("enter input"))

# for i in range(n):
#     for j in range(n)

n=int(input("Enter my input"))

for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print()    