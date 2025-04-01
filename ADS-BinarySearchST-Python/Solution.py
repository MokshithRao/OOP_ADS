class BinarySearchST:
    def __init__(self):
        self.keys = []
        self.values = []
        self.size_ = 0

    def isEmpty(self):
        return self.size_ == 0
    
    def size(self):
        return self.size_
    
    def insertion_sort(self):
        for i in range(1, len(self.keys)):
            for j in range(i, 0, -1):
                if self.keys[j] < self.keys[j - 1]:
                    self.keys[j], self.keys[j - 1] = self.keys[j - 1], self.keys[j]
                    self.values[j], self.values[j - 1] = self.values[j - 1], self.values[j]
                else:
                    break
    
    def binary_search(self, key):
        lo, hi = 0, self.size_ - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.keys[mid] < key:
                lo = mid + 1
            elif self.keys[mid] > key:
                hi = mid - 1
            else:
                return mid
        return None 

    def put(self, key, value):
        if self.size_ == 0:
            self.keys.append(key)
            self.values.append(value)
            self.size_ += 1
            self.insertion_sort()
        else:
            temp = self.binary_search(key)
            if temp is None:
                self.keys.append(key)
                self.values.append(value)
                self.size_ += 1
                self.insertion_sort()
            else:
                self.values[temp] = value

    def get(self, key):
        temp = self.binary_search(key)
        if temp is None:
            return None  
        return self.values[temp]
    
    def contains(self, key):
        temp = self.binary_search(key)
        return temp != None
     

    def delete(self, key):
        temp = self.binary_search(key)
        if temp is not None:
            self.keys.pop(temp)
            self.values.pop(temp)
            self.size_ -= 1

    def min(self):
        return self.keys[0] if self.size_ > 0 else None
    
    def max(self):
        return self.keys[self.size_ - 1] if self.size_ > 0 else None

    def floor(self, key):
        temp = self.binary_search(key)
        if temp is not None:
            return self.keys[temp]
        
        for i in range(self.size_ - 1, -1, -1):
            if self.keys[i] <= key:
                return self.keys[i]
        return None  

    def ceiling(self, key):
        temp = self.binary_search(key)
        if temp is not None:
            return self.keys[temp]
        
        for i in range(self.size_):
            if self.keys[i] >= key:
                return self.keys[i]
        return None  

    def rank(self, key):
        temp = self.binary_search(key)
        return temp if temp is not None else 0

    def select(self, k):
        return self.keys[k] if 0 <= k < self.size_ else None

    def deleteMin(self):
        if self.size_ > 0:
            self.keys.pop(0)
            self.values.pop(0)
            self.size_ -= 1

    def deleteMax(self):
        if self.size_ > 0:
            self.keys.pop(self.size_ - 1)
            self.values.pop(self.size_ - 1)
            self.size_ -= 1

    def size_range(self, key1, key2):
        index1 = self.binary_search(key1)
        index2 = self.binary_search(key2)
        if index1 is None or index2 is None:
            return 0
        return len(self.keys[index1:index2 + 1])

    def keys_all(self):
        return self.keys[:]

    def keys_range(self, key1, key2):
        index1 = self.binary_search(key1)
        index2 = self.binary_search(key2)
        if index1 is None or index2 is None:
            return []
        return self.keys[index1:index2 + 1]  