# class Queue:
#     def __init__(self,size):
#         self.size = size
#         self.queue = []

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def isFull(self):
#         return len(self.queue) == self.size

#     def enqueue(self,item):
#         if not self.isFull():
#             self.queue.append(item)
#         else:
#             return('Queue is Full')    

#     def dequeue(self):
#         if not self.isFull():
#             self.queue.pop(0)
#         else:
#             return("Queue is Empty nothing to delete")

#     def peek(self):
#         if not self.isEmpty():
#             return self.queue[0]
#         else:
#             return('Queue is Empty') 

#     def size(self):
#         return len(self.queue)

#     def displayqueue(self):
#         if not self.isEmpty():
#             return self.queue
#         else:
#             return('Queue is Empty')

# q = Queue(5)
# print(q.displayqueue())
# (q.enqueue('1234'))                
# (q.enqueue('1234'))
# (q.enqueue('1234'))
# (q.enqueue('1234'))
# (q.enqueue('1234'))
# print(q.enqueue('1234'))
# q.dequeue()
# print(q.displayqueue())
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.displayqueue())

## IsValidParenthesis

# def IsValidParenthesis(s):
#     stack = []
#     mapp = {
#         '}' : '{',
#         ']' : '[',
#         ')' :  "("
#     }

#     for bracket in s:
#         if bracket in mapp.values():
#             stack.append(bracket)
#         elif bracket in mapp.keys():
#             if not stack or stack[-1] != mapp[bracket]:
#                 return False
#             stack.pop()

#     return len(stack) == 0            

# string = '(){()}[]'
# print(IsValidParenthesis(string))