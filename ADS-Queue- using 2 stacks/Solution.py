class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size_ = 0

    def size(self):
        return self.size_
    
    def is_empty(self):
        return self.size_ == 0
    
    def add_first(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
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
    



class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.first_stack = Stack()
        self.second_stack = Stack()
        self.size = 0


    def peek(self):
        if self.size == 0:
            return None
        if self.first_stack.empty():
            self.push_and_pull()
        return self.second_stack.peek()
    
    def element(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        if self.second_stack.empty():
            self.push_and_pull()
        return self.second_stack.peek()
    

    def poll(self):
        if self.size == 0:
            return None
        if self.second_stack.empty():
            self.push_and_pull()
        self.size -= 1
        return self.second_stack.pop()
    

    def remove(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        if self.second_stack.empty():
            self.push_and_pull()
        self.size -= 1
        return self.second_stack.pop()
    

    def offer(self, element):
        if self.size >= self.capacity:
            return False
        self.first_stack.push(element)
        self.size += 1
        return True

    def add(self, element):
        if self.size >= self.capacity:
            raise FullQueueException("Queue is full")
        self.first_stack.push(element)
        self.size += 1
        return True

    def push_and_pull(self):
        while not self.first_stack.empty():
            self.second_stack.push(self.first_stack.pop())




class FullQueueException(Exception):
    def _init_(self, message):
        self.massage = message
        super()._init_(self.message)
    


