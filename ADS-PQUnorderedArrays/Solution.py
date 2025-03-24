def partition(a, lo, hi):  
    i = lo + 1
    j = hi
    v = a[lo]

    while True:
        while i <= j and a[i] <= v:
            i += 1

        while i <= j and a[j] >= v: 
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i] 
        else:
            break

    a[lo], a[j] = a[j], a[lo]  
    return j


def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        
        quick_sort(a, lo, p - 1)  
        quick_sort(a, p + 1, hi)  

def sort(a):
    quick_sort(a, 0, len(a) - 1)
    return a


class BinaryHeapPriorityQueue:
    def __init__(self):
        self.list = []
    
    def offer(self, e):
        if not self.list:
            self.list.append(e)
        else:
            self.list.append(e)
            self.list = sort(self.list)
        
    
    def add(self, e):
        self.offer(e)
    
    def clear(self):
        self.list.clear()
    
    def contains(self, o):
        if o in self.list:
            return o
    
    def iterator(self):
        return self.list
    
    def peek(self):
        if self.list is None:
            return None
        return self.list[0]
        
    
    def poll(self):
        element = self.list[0]
        if self.list is None:
            return None
        self.list.pop(0)
        return element
    
    
    def remove(self, o):
        if o in self.list:
            self.list.remove(o)
            return True
        return False
    
    def size(self):
        return len(self.list)
