# def ConvertToCaps(name):
#     nameCaps = name.upper()
#     return nameCaps

# name = input('enter name')
# callingTheFunction = ConvertToCaps(name)
# print(callingTheFunction)

# def add(nums,l,target):
#     for i in range(l):
#         for j in range(i+1,l):
#             if nums[i] + nums[j] == target:
#                 return([i,j])

# nums = [11,2,7,15]
# target = 9 
# l = len(nums)
# print(add(nums,l,target))

# def my_function():
#     print('hello,how are you')

# my_function()

# def my_function(name):
#   print(name + " syed")

# my_function("Emil")
# my_function("Tobias")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def name(*fun):
#     print('youngest child is ' + fun[2])

# name('krishna','meghnanth','imran','jaya') 

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my_function():
#   print("Hello from a function")

# my_function()

# def my_function(name):
#   print(name + ' Syed')

# my_function('Imran')
# my_function("Hania")
# my_function("Ammi")

# def home(add,don):
#   print(add,'my',don)

# home(195,'peta')  

#Accesing in Fun

# def Access(*arg):
#   print('younger boy in house is ' + arg[2])

# Access('imr','an','sd')  

# So many keyword Arg

# def dic(**kw):
#   print('Elder boy in house '+kw['child1'])

# dic(child0 = 'imr',child1 = 'ans')

# def multi(x):
#   print(5 * x)

# multi(4)
# multi(2)  

# def fruit(food):
#   for i in food:
#     print(i,end='')
# fru = ['a','b','c','d']
# fruit(fru)

def square( item_list ):       
    squares = [ ]    
    for l in item_list:    
        squares.append( l**2 )    
    return squares    
    
my_list = [17, 52, 8];    
my_result = square( my_list )    
print( "Squares of the list are: ", my_result )