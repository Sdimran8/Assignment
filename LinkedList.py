class Head:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        newHead = Head(data)
        if self.isEmpty():
            self.head = newHead
            return
        
        current = self.head
        while current.next:
            current = current.next
        else:
            current.next = newHead

    def prepend(self, data):
        newHead = Head(data)
        newHead.next = self.head
        self.head = newHead

    def insert_at_any_position(self, value, position):
        newHead = Head(value)
        if position == 0:
            newHead.next = self.head
            self.head = newHead

        else:
            current = self.head

            for i in range(position-1):
                if current is None:
                    return("index out of range")
                else:
                    current = current.next

            newHead.next = current.next
            current.next = newHead

    def displayLl(self):
        current = self.head
        while current is not None:
            print(current.data, end = "-->")
            current = current.next
        print("None")

    def delete(self, data):
        if self.isEmpty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


ll = LinkedList()
ll.append(765)
ll.append(76)

ll.prepend(23)
ll.delete(76)
ll.insert_at_any_position(87,1)
ll.displayLl()


 

