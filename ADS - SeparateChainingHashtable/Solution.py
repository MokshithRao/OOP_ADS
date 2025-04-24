class SeparateChainingHashST:
    class Node:
        def __init__(self, key, val, next_node):
            self.key = key
            self.val = val
            self.next = next_node

    def __init__(self, m=4):
        self.n = 0
        self.m = m
        self.st = [None] * m

    def _hash(self, key):
        return (hash(key) & 0x7fffffff) % self.m

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def get(self, key):
        if key is None:
            return None
        i = self._hash(key)
        x = self.st[i]
        while x:
            if x.key == key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        if key is None:
            return
        if val is None:
            self.delete(key)
            return
        if self.n >= 10 * self.m:
            self._resize(2 * self.m)
        i = self._hash(key)
        x = self.st[i]
        while x:
            if x.key == key:
                x.val = val
                return
            x = x.next
        self.st[i] = self.Node(key, val, self.st[i])
        self.n += 1

    def delete(self, key):
        if key is None:
            return
        i = self._hash(key)
        self.st[i] = self._delete(self.st[i], key)
        if self.m > 4 and self.n <= 2 * self.m:
            self._resize(self.m // 2)

    def _delete(self, x, key):
        if x is None:
            return None
        if x.key == key:
            self.n -= 1
            return x.next
        x.next = self._delete(x.next, key)
        return x

    def contains(self, key):
        return self.get(key) is not None

    def keys(self):
        keys_list = []
        for i in range(self.m):
            x = self.st[i]
            while x:
                keys_list.append(x.key)
                x = x.next
        return keys_list

    def _resize(self, chains):
        temp = SeparateChainingHashST(chains)
        for key in self.keys():
            temp.put(key, self.get(key))
        self.m = temp.m
        self.n = temp.n
        self.st = temp.st
