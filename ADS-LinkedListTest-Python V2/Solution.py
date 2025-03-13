class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        

    def add_first(self, s):
        new_node = Node(s)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1


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
        return self.size
    
    def remove(self):
        if not self.head:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1

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

        self.size -= 1
        return removed_data


    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


    def find_middle(self):
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    

    def nth_from_end(self, n):
        if n <= 0 or n > self.size:
            return None
    
        main = self.head
        ref = self.head
        for _ in range(n):
            if not ref:
                return None
            ref = ref.next
        while ref:
            main = main.next
            ref = ref.next
        return main.data
    

    
    def insert_at_position(self, index, s):
        if index > self.size or index < 0:
            return None
        
        new_node = Node(s)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
                
        self.size += 1


    def insert_before(self, target, s):
        if not self.head:
            return 
        
        if self.head.data == target:
            self.add_first(s)
            return
        
        current = self.head
        while current.next and current.next.data != target:
            current = current.next
        if current.next:
            new_node = Node(s)
            new_node.next = current.next
            current.next = new_node
            self.size += 1


    def delete_after(self, target):
        current = self.head
        while current and current.data != target:
            current = current.next

        if current and current.next:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self.size -= 1


    def to_string(self):
        if self.size == 0:
            return "LinkedList is empty"
        
        l = []
        current = self.head
        while current:
            l.append(f"[{str(current.data)}]")
            current = current.next
        return "".join(l)