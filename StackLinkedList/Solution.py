class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def size(self):
        return self.size_
    
    def is_empty(self):
        return self.size_ == 0
    
    def add_first(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size_ += 1

    def remove_first(self):
        if self.head is None:
            return None
        
        removed = self.head.data
        self.head = self.head.next
        self.size_ -= 1
        return removed
    
    def contains(self, e):
        current = self.head
        while current:
            if current.data == e:
                return True
            current = current.next
        return False


        
    


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def empty(self):
        return self.stack.is_empty()
    
    def peek(self):
        if self.stack.is_empty():
            raise IndexError("empty stack")
        return self.stack.head.data
    
    def pop(self):
        if self.stack.is_empty():
            raise IndexError("empty stack")
        else:
            removed = self.stack.head.data
            self.stack.remove_first()
            return removed

    def push(self, item):
        self.stack.add_first(item)
        return item

    def search(self, o):
        current = self.stack.head
        position = 1
        while current:
            if current.data == o:
                return position
            current = current.next
            position += 1
        return -1