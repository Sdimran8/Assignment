# LINEAR SEARCH

# a = [1,85,3,5,8]
# res = 8
# for i in range(len(a)):
#     if a[i] == res:
#         print(f'p {res}',i)

# Binaray Search

# def binarySearch(a,t,l):
#     start = 0
#     end = l-1
#     while start <= end:
#         mid = (start+end)//2
#         if t == a[mid]:
#             return mid
#         elif t >= a[mid]:
#             start = mid +1
#         elif t <= a[mid]:
#             end = mid - 1
#     else:
#         print("Target not found")

# arr = [11,22,33,44,55,66,77]                        
# targer = 66
# leng = len(arr)
# print(binarySearch(arr,targer,leng))

# import math
# a = 12.65
# print(math.ceil(a)) # Get the next num

# import math
# a = 2.34
# print(math.floor(a)) # get the rounded value of same num -

# import math
# a = 16
# print(int(math.sqrt(a)))

#Jump Search :

# import math

# def jumpSearch(a,t,l):
#     step = int(math.sqrt(l))
#     previous = 0
#     while a[min(step,l)-1]<t:
#         previous = step
#         step = step + int(math.sqrt(l))
#         if previous >= l:
#             return ("Not Found")

#     for i in range(previous,min(step,l)):
#         if a[i] == t:
#             return(i)
#     return("Not Found")        

# a = [1,5,67,87,67,25,4,54,6,765,864]
# b = sorted(a)
# print(b)
# t = 67
# l = len(a)
# print(jumpSearch(b,t,l))

# Bubble Sort:

# def bubbleSort(arr):
#     l = len(arr)
#     for i in range(l):
#         for j in range(0,l-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

# arr = [5,1,4,2,8]
# res = bubbleSort(arr)
# print(arr)                

# Selection Sort :

# def selectionSort(arr,l):
#     for i in range(l):
#         minIndex = i 
#         for j in range(i+1,l):
#             if arr[j] < arr[minIndex]:
#                 minIndex = j
#         arr[i],arr[minIndex] = arr[minIndex],arr[i]

# arr = [5,1,4,2,445,65,6]
# l = len(arr)
# res = (selectionSort(arr,l))
# print(arr)

# Insertion Sort :

# def insertionSort(arr,l):
#     for i in range(1,l):
#         temp = arr[i]
#         j = i-1
#         while j>=0 and temp < arr[j]:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = temp

# arr = [5,1,4,2,445,65,6]
# l = len(arr)
# res = (insertionSort(arr,l))
# print(arr)        
