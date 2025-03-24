class BinaryHeapPriorityQueue:
    def __init__(self):
        self.list = []
    
    def offer(self, e):
        self.list.append(e)
        
    
    def add(self, e):
        self.offer(e)
    
    def clear(self):
        self.list.clear()
    
    def contains(self, o):
        if o in self.list:
            return o
    
    def iterator(self):
        return sorted(self.list)
    
    def peek(self):
        if self.list is None:
            return None
        
        min = 9999999999
        for i in self.list:
            if i < min:
                min = i
        return min
        
    
    def poll(self):
        if self.list is None:
            return None
        min = 99999999999
        for i in self.list:
            if i < min:
                min = i
        self.list.pop(min)
        return min
    
    
    def remove(self, o):
        l = []
        for i in self.list:
            if i == o:
                continue
            l.append(i)
            return True
        self.list = l
        return False
    
    def size(self):
        return len(self.list)
