class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self,value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head

        self._size+=1


    def add_first(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = new_node

        self._size += 1


    def contains(self,value):
        current = self.head
        c = 0

        while c < self._size:
            if current.value == value:
                return True
            current = current.next
            c += 1
        return False
    

    def get_first(self):
        return self.head.value
    
    def get_last(self):
        return self.tail.value
    
    def size(self):
        return self._size
    
    def remove(self):
        if not self.head:
            return None
        
        removable = self.head.value
        self.head = self.head.next
        self._size -= 1
        
        return removable
    

    def remove_last(self):
        if self.head is None:  
            return None
        
        removable = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removable
    

    def remove_at(self,index):
        if self.head is None:  
            return None
        
        if self.head == self.tail:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        
        if current == self.head:
            self.remove()
        elif current == self.tail:
            self.remove_last()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self._size -= 1
    

    def get(self, index):
        if index < 0 or index >= self._size:
            return
        
        Current = self.head
        for i in range(index):
            Current = Current.next
        return Current.value
    

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0


    def is_circular(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


    def __str__(self):
        if self._size == 0:
            return "CircularLinkedList is empty"

        current = self.head
        l = []
        count = 0

        while count < self._size:
            l.append(f"[{current.value}]")
            current = current.next
            count+=1
        return "<->".join(l)
    


class Josephus:
    def josephusDCLL(self, size, rotation):
        self.size = size
        self.rotation = rotation
        LL = DoublyCircularLL()

        for i in range(1,size + 1):
            LL.add(i)

        current = 0

        for i in range(size - 1):
            current = (current + rotation - 1) % LL.size()
            LL.remove_at(current)
        return LL.get_first()
