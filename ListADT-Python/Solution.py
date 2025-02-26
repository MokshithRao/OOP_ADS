class ArrayListADT:
    def __init__(self) -> None:
        self.data = []
        # self.size = len(self.data)

    def add(self, e):
        self.data.append(e)
        return True


    def add_at(self, index, element):
        # print(self.size)
        self.data.append(0)
        self.size = len(self.data)
        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = element
        # print(self.data)
        return True

    def addAll(self, index, c):
        for i in range(len(c)):
            self.add_at(index + i, c[i])
        return True


    def clear(self):
        self.data = []
        self.size = 0
        


    def contains(self, o):
        for i in self.data:
            if i == o:
                return True
        return False


    def ensureCapacity(self, minCapacity):
        self.addAll(len(self.data), [None]*minCapacity)


    def get(self, index):
        # for i in range(len(self.data)):
        #     if i == index:
        return self.data[index]


    def __str__(self) -> str:
        return f"{self.data}"