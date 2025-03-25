class BinaryHeapPriorityQueue:
    def __init__(self):
        self.array = []
        self.size1 = 0

    def add(self, ele):
        self.array.append(ele)
        self.size1 += 1
        self.swim(self.size1 - 1)
    
    def offer(self, ele):
        self.add(ele)

    def size(self):
        return self.size1
    
    def contains(self, ele):
        for i in self.array:
            if i == ele:
                return True
        return False
    
    def index_of(self, ele):
        for i in range(len(self.array)):
            if self.array[i] == ele:
                return i
        return None
    
    def peek(self):
        return self.array[0]
    
    def poll(self):        
        root = self.array[0]
        self.array[0] = self.array[self.size1 - 1]
        self.size1 -= 1
        self.array.pop()
        self.sink(0)
        return root
    
    def remove(self, ele):
        index = self.index_of(ele)        
        self.array[index] = self.array[self.size1 - 1]
        self.size1 -= 1
        self.array.pop()
        self.sink(index)
        self.swim(index)
        return True
    
    def clear(self):
        self.array = []
        self.size1 = 0

    def iterator(self):
        return self.array
    
    def __str__(self):
        return f"{self.array}"

    def swim(self, index):
        while index > 0 :
            parent = (index-1)//2
            if self.array[index] < self.array[parent]:
                self.array[index], self.array[parent] = self.array[parent], self.array[index]
                index = parent
            else:
                break
    
    def sink(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        s = index
        
        if left < self.size1 and self.array[left] < self.array[s]:
            s = left
        
        if right < self.size1 and self.array[right] < self.array[s]:
            s = right
        
        if s != index:
            self.array[index], self.array[s] = self.array[s], self.array[index]
            self.sink(s)