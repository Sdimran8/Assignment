# class stack:
#     def __init__(self,size):
#         self.items = []
#         self.size = size

#     def isStackFull(self):
#         if self.size is None:
#             return False
#         else:
#             return len(self.items) == self.size

#     def addElement(self,item):
#         if len(self.items) <= self.size:
#             self.items.append(item)
#         else:
#             print('stack is full')

#     def removeElement(self):
#         if len(self.items) == 0:
#             print('stack is empty add element to remove it')
#         else:
#             self.items.pop()

#     def peek(self):
#         if len(self.items) == 0:
#             return('stack is empty')
#         else:    
#             return self.items[-1][(self.items)-1] 

#     def printStack(self):
#         print(self.items)

# s = stack(5)
# s.addElement(1) 
# s.addElement(2)        
# s.addElement(3)        
# s.addElement(4)        
# s.addElement(5)
# s.printStack()
# s.removeElement()
# s.printStack()  
# s.removeElement()
# s.printStack()               

# LINEAR SEARCH
# a = [1,85,3,5,8]
# res = 8
# for i in range(len(a)):
#     if a[i] == res:
#         print(f'p {res}',i)

# Binaray Search

def binarySearch(a,t,l):
    start = 0
    end = l-1
    while start <= end:
        mid = (start+end)//2
        if t == a[mid]:
            return mid
        elif t >= a[mid]:
            start = mid +1
        elif t <= a[mid]:
            end = mid - 1
    else:
        print("Target not found")

arr = [11,22,33,44,55,66,77]                        
targer = 66
leng = len(arr)
print(binarySearch(arr,targer,leng))

# import math
# a = 12.65
# print(math.ceil(a)) # Get the next num

# import math
# a = 2.34
# print(math.floor(a)) # get the rounded value of same num -

# import math
# a = 16
# print(int(math.sqrt(a)))