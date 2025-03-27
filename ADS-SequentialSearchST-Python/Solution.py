class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class SequentialSearchST:
    def __init__(self):
        self.head = None
        self.size_ = 0

    def isEmpty(self):
        return self.size_ == 0
    
    def size(self):
        return self.size_
    

    def put(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value, self.head)
        self.head = new_node
        self.size_ += 1

    

    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def contains(self, key):
        return self.get(key) is not None
    
    def delete(self, key):
        if not self.head:
            return
        if self.head.key == key:
            self.head = self.head.next
            self.size_ -= 1
            return
        
        prevs, current = None, self.head
        while current:
            if current.key == key:
                prevs.next = current.next
                self.size_ -= 1
                return
            prevs, current = current, current.next

    
    def min(self):
        if self.isEmpty():
            return None
        minimum = self.head.key
        current = self.head.next
        while current:
            if current.key < minimum:
                minimum = current.key
            current = current.next
        return minimum
    

    def max(self):
        if self.isEmpty():
            return None
        maximun = self.head.key
        current = self.head.next
        while current:
            if current.key > maximun:
                maximun = current.key
            current = current.next
        return maximun
    

    def floor(self, key):
        floor_key = None
        current = self.head
        while current:
            if current.key <= key and (floor_key is None or current.key > floor_key):
                floor_key = current.key
            current = current.next
        return floor_key
    
    def ceiling(self, key):
        ceiling_key = None
        current = self.head
        while current:
            if current.key >= key and (ceiling_key is None or current.key < ceiling_key):
                ceiling_key = current.key
            current = current.next
        return ceiling_key
    
    def rank(self, key):
        c = 0
        current = self.head
        while current:
            if current.key < key:
                c += 1
            current = current.next
        return c
    
    def select(self, k):
        list_keys = self.keys()
        list_keys.sort()
        if 0 <= k < len(list_keys):
            return list_keys[k]
        return None
    
    def deleteMin(self):
        min_key = self.min()
        if min_key is not None:
            self.delete(min_key)
    
    def deleteMax(self):
        max_key = self.max()
        if max_key is not None:
            self.delete(max_key)
    
    def size_range(self, lo, hi):
        count = 0
        current = self.head
        while current:
            if lo <= current.key <= hi:
                count += 1
            current = current.next
        return count
    
    def keys(self):
        keys_list = []
        current = self.head
        while current:
            keys_list.append(current.key)
            current = current.next
        return keys_list
    
    def keys_range(self, lo, hi):
        keys_list = []
        current = self.head
        while current is not None:
            if lo <= current.key <= hi:
                keys_list.append(current.key)
            current = current.next
        
        keys_list.sort()
        return keys_list

