#append

# list_a = []
# for i in range(1,5):
#     list_a.append(i)
# print(list_a)    

# a = ['apple','banana','cat']
# a.append('dog')
# print(a)

# a = ['apple','boy','cow']
# b = ['fish','hen','goat']
# a.append(b)
# print(a)

# num = [1,2,3]
# num.append('four')
# print(num)

# l = ['one','two','three']
# l.append('four')
# print(l)

#Extend

# fruits = ['apple', 'banana', 'cherry']
# points = (1, 4, 5, 9)
# fruits.extend(points)
# print(fruits)

# languages = ['Tel','Hin','Eng']
# lan=['spanish','germany']
# languages.extend(lan)
# print(languages)

# a=['one','two']
# b=['three']
# a.extend('three')
# print(a)

# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.extend(l2)
# print(l1)

# j = ['for','i']
# k =['range','of',1]
# j.extend(k)
# print(j)

#Insert 

# a = [1,2,3]
# a.insert(1,4)
# print(a)

# k = ['water','bottle']
# k.insert(2,'pack')
# print(k)

# h =['soap','sandal']
# h.insert(0,'paste')
# print(h)

# a = ['app','software']
# a.insert(5,'pop')
# print(a)

# h = ['k','k','o','u']
# (h.insert(1,2))
# print(h)

#Remove

# i = [1,2,3,4,2]
# i.remove(2)
# print(i)

# h = ['six','x','y','x']
# h.remove('x')
# print(h).

# k = [1,3.5,7]
# k.remove(9)
# print(k)
 
# s = ['list','for','the','list'] 
# s.remove('list')
# print(s)

# q = [1,'one',2,'one']
# q.remove('one')
# print(q)

# l = [1,2,3,3,4,5,1,2,9]
# n = int(input('enter the value'))
# if n in l:
#     print(n,'is available at the first occurence is at :',l.index(n))
# else:
#     print('not exist')        

# l = [1,2,3,4,5,6,7,8,9,10]
# n = int(input('enter input'))
# if n in l:
#     l.remove(n)
#     print(l)

# elif n not in l:
#     print('deletd')

# else:
#     print('out of range')    


# s ='pyThon is EaSy LanGuaGe'
# count = 0
# for i in s:
#     if i.isupper():
#         print(i.count(i))
#     count = count + 1
    # elif i.islower():
        # print(i)           
# print(s.upper())

# s ='pyThon is EaSy LanGuaGe'
# count = ''
# for i in s:
#     if i.isupper():
#         print(count(i))
#     # elif i.islower():
#         count = count + 1
# print(i) 

# n ='pyTHoNSSSS'
# print('capital letters : ', sum (1 for i in n if i.isupper()))   

n = 'imRddddddaKPUn'
sum = 0 
for i in n :
    if i.islower():
        sum = sum + 1
print(sum)

