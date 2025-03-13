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