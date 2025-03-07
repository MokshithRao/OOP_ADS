class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Steque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1


    def pop(self):
        if not self.head:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return removed_data
    

    def enqueue(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0



    def __str__(self):
        if self._size == 0:
            return "Steque is empty"

        Current = self.head
        l = []
        while Current:
            l.append(f"[{str(Current.data)}]")
            Current = Current.next
        return "".join(l)
