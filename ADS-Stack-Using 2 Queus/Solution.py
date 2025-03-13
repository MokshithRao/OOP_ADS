class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_LL = 0

    def add_last(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size_LL += 1
        

    def add_first(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size_LL += 1


    def contains(self, s):
        current = self.head
        while current:
            if current.data == s:
                return True
            current = current.next
        return False
    
    def get_first(self):
        if self.head:
            return self.head.data
        return None
    
    def get_last(self):
        if self.tail:
            return self.tail.data
        return None
    
    def size(self):
        return self.size_LL
    
    def remove(self):
        if not self.head:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        self.size_LL -= 1

        return removed_data
    
    def remove_last(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        else:
            Current = self.head
            while Current.next != self.tail:
                Current = Current.next
            removed_data = self.tail.data
            self.tail = Current
            self.tail.next = None

        self.size_LL -= 1
        return removed_data


    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size_LL = 0

    def __str__(self):
        if self.size_LL == 0:
            return "LinkedList is empty"
        
        l = []
        current = self.head
        while current:
            l.append(f"[{str(current.data)}]")
            current = current.next
        return "".join(l)
    


class MyQueue:
    def __init__(self, capacity):
        self.queue = MyLinkedList()
        self.capacity = capacity
        self.size = 0

    def peek(self):
        if self.queue.head is None:
            return None
        return self.queue.head.data
    
    def poll(self):
        if self.queue.head is None:
            return None
        removed = self.queue.head.data
        self.queue.remove()
        self.size -= 1
        return removed
    

    def element(self):
        if self.queue.head is None:
            raise IndexError("Empty Queue")
        return self.queue.head.data
    
    def remove(self):
        if self.queue.head is None:
            raise IndexError("Empty Queue")
        removed = self.queue.head.data
        self.queue.remove()
        self.size -= 1
        return removed
    
    def add(self,e):
        if self.size == self.capacity:
            raise FullQueueException("Queue is Full")
        self.queue.add_last(e)
        self.size += 1
        return True
    

    def offer(self, e):
        if self.size == self.capacity:
            return None
        self.queue.add_last(e)
        self.size += 1
        return True

    def __str__(self):
        return f"{self.queue}"


class FullQueueException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




class Stack:
    def __init__(self, capacity=10):
        self.queue1 = MyQueue(capacity)
        self.queue2 = MyQueue(capacity)
        self.capacity = capacity
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, item):
        if self.size == self.capacity:
            raise FullQueueException("Stack is Full")
        self.queue1.add(item)
        self.size += 1
        return item

    def pop(self):
        if self.empty():
            raise IndexError("Empty Stack")
        
        while self.queue1.size > 1:
            self.queue2.add(self.queue1.poll())
        
        popped_item = self.queue1.poll()
        self.size -= 1
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item

    def peek(self):
        if self.empty():
            raise IndexError("Empty Stack")
        
        while self.queue1.size > 1:
            self.queue2.add(self.queue1.poll())
        
        top_item = self.queue1.peek()
        self.queue2.add(self.queue1.poll())
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_item

    def search(self, item):
        position = -1
        index = self.queue1.size
        
        current = self.queue1.queue.head
        while current:
            if current.data == item:
                position = index
            index -= 1
            current = current.next
        
        return position

    def __str__(self):
        return f"{self.queue1}"

