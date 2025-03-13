class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add_to_front(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1


    def add_to_end(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None 
        self._size += 1


    def remove_from_front(self):
        if not self.head:
            return None
        
        removed_data = self.head.value
        self.head = self.head.next
        self.head.prev = None 
        self._size -= 1

        return removed_data


    def remove_from_end(self):
        if not self.tail:
            return None
        
        removed = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removed
    
    
    def get_size(self):
        return self._size

    def find(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False
    

    def insert_at(self, index, value):
        if index > self._size or index < 0:
            return 
        
        if index == 0:
            self.add_to_front(value)
            return
        
        if index == self._size:
            self.add_to_end(value)
            return
        
        new_node = Node(value)
        current = self.head
        for i in range(index-1):
            current = current.next
        current.next.prev = new_node
        new_node.prev = current
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        

    def remove_at(self, index):
        if index < 0 or index >= self._size:
            return
        
        if self.head == self.tail:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        if current.next is None:
            self.remove_from_end()
            return
        x = current.next
        y = current.prev
        current.prev.next = x
        current.next.prev = y
        self._size -= 1
        


    def get_size(self):
        return self._size
    

    def reverse_traversal(self):
        current =self.tail
        while current:
            print(current.value,end=" ")
            current = current.prev
        print()


    def print_list(self):
        if self._size == 0:
            return
        
        l = []
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
    

    def check_empty(self):
        # return self._size == 0
        if self.head == None:
            return True
        return False

    
    def clear_list(self):
        self.head = None
        self.tail = None
        self._size = 0

    def get_at(self, index):
        if index < 0 or index >= self._size:
            return
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    
    def get_node_at(self, index):
        if index < 0 or index >= self._size:
            return
        current = self.head
        for i in range(index):
            current = current.next
        return current
    
    def swap_nodes(self, index1, index2):
        if index1 == index2:
            return
        node1 = self.get_node_at(index1)
        node2 = self.get_node_at(index2)
        if node1 == None or node2 == None:
            return
        
        self.insert_at(index1,node2.value)
        self.remove_at(index1+1)
        self.insert_at(index2,node1.value)
        self.remove_at(index2+1)
        


    def detect_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False
    
    def __str__(self):
        if self._size == 0:
            return "DoublyLinkedList is empty"

        current = self.head
        ele = []

        while current:
            ele.append(f"[{current.value}]")
            current = current.next
        return "<->".join(ele)
    
    
            