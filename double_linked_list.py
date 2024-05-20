class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None



class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    
    def insert_at_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        
            current = self.head
            while current and current.next:
                current = current.next
            self.tail = current
        
        self.size += 1

    def insert_at_end(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def print_list_of_item(self):
        current = self.head
        while current:
            print('value:', current.value)
            current = current.next
        


dli = DoublyLinkedList()

item = [1,2,3,4,5]

for num in item:
    dli.insert_at_begin(num)

print('after insert at begin:')
dli.print_list_of_item()

item = [1,2,3,4,5]

for num in item:
    dli.insert_at_end(num)

print('after insert at end:')
dli.print_list_of_item()

