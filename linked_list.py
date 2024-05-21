class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    

    def insert(self, value):
        node = Node(value)

        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            temp = self.tail
            self.tail = node
            temp.next = self.tail
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.value

    
    def print_list_of_item(self):
        current = self.head

        while current:
            print('value:',current.value)
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current.value
            current = current.next
        return None
    

li = LinkedList()

item = [1,2,3,4,5]
# item = [1]

for num in item:
    li.insert(num)


li.print_list_of_item()

print('pop:',li.pop())
print('after pop:')
li.print_list_of_item()
print('search item 6:', li.search(6))
print('search item 3:', li.search(3))










