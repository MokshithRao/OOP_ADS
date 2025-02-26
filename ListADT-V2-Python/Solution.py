class ArrayListADT:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def add(self, e):
        # if e not in self.data:
        self.data.append(e)
        self.size += 1
        return True


    def add_at(self, index, element):
        # print(self.size)
        self.data.append(0)
        self.size +=1 
        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = element
        # print(self.data)
        return True

    def add_all_at(self, index, c):
        for i in range(len(c)):
            self.add_at(index + i, c[i])
        return True

    def add_all(self, c):
        for i in c:
            self.data.append(i)
        # self.data.extend(c)
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
        # print(self.data)
        l = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                l.append(self.data[i])

        self.size = len(l)
        self.data = l
        return l[index]

    def index_of(self, o):
        # print(self.data)
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1
    
    def last_index_of(self, o):
        l = []
        # print(self.data)
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
                # print(l[-1])
        return l[-1]
    
    def size_(self):
        return self.size
    
    def is_empty(self):
        # print(len(self.data))
        return len(self.data) == 0
    
    def remove_at(self,index):
        # print(self.data)
        l = []
        ind = 0
        # print(self.data, l)
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
        
        # l = []
        # for i in self.data:
        #     if i == o:
        #         continue
        #     else:
        #         l.append(i)
        # self.data = l
        # self.size = len(self.data)
        # return True

                
    def set(self, index, element):
        old_ele = self.data[index]
        self.data[index] = element
        return old_ele
        # l = []
        # old_ele = 0

        # for i in range(len(self.data)):
        #     if i != index:
        #         l.append(self.data[i])
        #     else:
        #         l.append(element)
        #         old_ele = self.data[index]
        # self.data = l
        # self.size = len(self.data)
        # return old_ele
    

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
    


    