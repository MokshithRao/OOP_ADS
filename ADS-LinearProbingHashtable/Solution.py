class LinearProbingHashST:
    def __init__(self, init_capacity=4):
        self._count = 0
        self._capacity = init_capacity
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._order = []

    def _index(self, key):
        return (hash(key) & 0x7fffffff) % self._capacity

    def _resize(self, new_cap):
        temp = LinearProbingHashST(new_cap)
        for key in self._order:
            if self.get(key) is not None:
                temp.put(key, self.get(key))
        self._keys = temp._keys
        self._values = temp._values
        self._capacity = temp._capacity
        self._order = temp._order

    def put(self, key, value):
        if self._count >= self._capacity // 2:
            self._resize(self._capacity * 2)

        i = self._index(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                self._values[i] = value
                return
            i = (i + 1) % self._capacity
            
        self._keys[i] = key
        self._values[i] = value
        if key not in self._order:
            self._order.append(key)
        self._count += 1

    def get(self, key):
        i = self._index(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._capacity
        return None


    def contains(self, key):
        return self.get(key) is not None


    def delete(self, key):
        if not self.contains(key):
            return
        
        i = self._index(key)
        while self._keys[i] != key:
            i = (i + 1) % self._capacity

        self._keys[i] = None
        self._values[i] = None
        self._count -= 1

        self._order.remove(key)
        i = (i + 1) % self._capacity
        while self._keys[i] is not None:
            k = self._keys[i]
            v = self._values[i]
            self._keys[i] = None
            self._values[i] = None
            self._count -= 1
            self.put(k, v)
            i = (i + 1) % self._capacity


        if 0 < self._count <= self._capacity // 8:
            self._resize(self._capacity // 2)

    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def keys_iter(self):
        return sorted(self._order, key=lambda x: len(x))
