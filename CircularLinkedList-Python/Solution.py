class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self._size += 1


    def add_first(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self._size += 1

    def contains(self, s):
        current = self.head
        c = 0
        while c < self._size:
            if current.value == s:
                return True
            current = current.next
            c += 1
        return False
    
    def get_first(self):
        if self.head:
            return self.head.value
        return None
    
    def get_last(self):
        if self.tail:
            return self.tail.value
        return None
    
    def size(self):
        return self._size
    
    def remove(self):
        if self.head is None:
            return None
        
        removed = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self._size -= 1
        return removed
    
    def remove_last(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            removed = self.head.value
            self.head = None
            self.tail = None
            self._size -= 1
            return removed

        current = self.head
        while current.next != self.tail:
            current = current.next
        removed = self.tail.value
        self.tail = current
        self.tail.next = self.head
        self._size -= 1
        return removed
        
    def get(self, index):
        if index < 0 or index >= self._size:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0


    def __str__(self):
        if self._size == 0:
            return "CircularLinkedList is empty"
        
        current = self.head
        l = []
        count = 0
        while count < self._size:
            l.append(f"[{current.value}]")
            current = current.next
            count += 1
        return "<->".join(l)
    
    def is_circular(self):
        if self.head is None:
            return False
        
        current = self.head
        while current.next != self.head:
            current = current.next
        
        return current.next == self.head
