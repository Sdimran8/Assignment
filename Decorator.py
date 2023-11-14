#LinkedList

def greet(c):
    def wrapper():
        print('hey bro')
        c()
    return wrapper
@greet            

def greetreply():
    print('Hi,How you doiung..??')

greetreply()

#Linked list Bubble Sort:
