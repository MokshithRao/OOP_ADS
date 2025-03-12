class ArrayListADT:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def add(self, e):
        self.data.append(e)
        self.size += 1
        return True


    def add_at(self, index, element):
        self.data.append(0)
        self.size +=1 
        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = element
        return True

    def add_all_at(self, index, c):
        for i in range(len(c)):
            self.add_at(index + i, c[i])
        return True

    def add_all(self, c):
        for i in c:
            self.data.append(i)
        self.size += len(c)
        return True


    def clear(self):
        self.data = []
        self.size = 0
        

    def contains(self, o):
        for i in self.data:
            if i == o:
                return True
        return False


    def ensure_capacity(self, minCapacity):
        if len(self.data) < minCapacity:
            self.add_all_at(len(self.data), [None]*(minCapacity - len(self.data)))
        

    def get(self, index):
        l = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                l.append(self.data[i])

        self.size = len(l)
        self.data = l
        return l[index]

    def index_of(self, o):
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1
    
    def last_index_of(self, o):
        l = []
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
        return l[-1]
    
    def size_(self):
        return self.size
    
    def is_empty(self):
        return len(self.data) == 0
    
    def remove_at(self,index):
        l = []
        ind = 0
        for i in range(len(self.data)):
            if i != index:
                l.append(self.data[i])
            else:
                ind += self.data[i]
        self.data = l
        self.size = len(self.data)
        return ind

    def remove(self, o):
        self.data.remove(o)
        self.size = len(self.data)
        return True

                
    def set(self, index, element):
        old_ele = self.data[index]
        self.data[index] = element
        return old_ele
        

    def trim_to_size(self):
        l = []
        for i in self.data:
            if i == None:
                continue
            else:
                l.append(i)
        self.data = l
        self.size = len(self.data)
        return len(self.data) == self.size


    def __str__(self) -> str:
        return f"{self.data}"
    



class MyQueue:
    def __init__(self, capacity):
        self.queue = ArrayListADT()
        self.capacity = capacity
        self.front = 0
        self.back = 0
        self.size = 0


    def add(self, e):
        if self.size == self.capacity:
            raise FullQueueException("Empty Queue")
        else:
            self.queue.add(e)
            self.back += 1
            self.size += 1
            return True
        

    def peek(self):
        if self.size == 0:
            return None
        return self.queue.get(self.front)
    
    def poll(self):
        if self.size == 0:
            return None
        else:
            removed = self.queue.get(self.front)
            self.remove()
            return removed
        
    def element(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        return self.queue.get(self.front)
    

    def remove(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        removed = self.queue.get(self.front)
        self.front += 1
        self.size -= 1
        return removed
    
    def offer(self, e):
        if self.size == self.capacity:
            return False
        self.queue.add(e)
        self.size += 1
        return True
    
class FullQueueException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    