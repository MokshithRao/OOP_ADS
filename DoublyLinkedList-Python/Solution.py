class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def add(self, s):
        new_node = Node(s)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1


    def add_first(self, s):
        new_node = Node(s)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1


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
        return self._size


    def remove(self):
        if not self.head:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        
        return removed_data


    def remove_last(self):
        if not self.head:
            return None
        
        removed = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self._size -= 1
        return removed


    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0



    def __str__(self):
        if self._size == 0:
            return "DoublyLinkedList is empty"
        
        l = []
        current = self.head
        while current:
            l.append(f"[{(current.data)}]")
            current = current.next
        return "<->".join(l)
        
