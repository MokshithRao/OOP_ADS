class Node:
    def __init__(self, key, value, size=1):
        self.key = key
        self.value = value
        self.size = size  
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def get(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def contains(self, key):
        value = self.get(key)  
        if value is None:  
            return False
        else: 
            return True

    def min(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        return self._min(self.root).key

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        return self._max(self.root).key

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def floor(self, key):
        node = self._floor(self.root, key)
        if node is None:
            raise ValueError("No floor exists")
        return node.key

    def _floor(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        return t if t else node

    def floor2(self, key):
        node = self.root
        floor = None
        while node:
            if key == node.key:
                return node.key
            elif key < node.key:
                node = node.left
            else:
                floor = node
                node = node.right
        if floor is None:
            raise ValueError("No floor exists")
        return floor.key

    def ceiling(self, key):
        node = self._ceiling(self.root, key)
        if node is None:
            raise ValueError("No ceiling exists")
        return node.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key > node.key:
            return self._ceiling(node.right, key)
        t = self._ceiling(node.left, key)
        return t if t else node

    def select(self, k):
        if k < 0 or k >= self.size():
            raise ValueError("Invalid rank")
        return self._select(self.root, k).key

    def _select(self, node, k):
        if node is None:
            return None
        left_size = self._size(node.left)
        if k < left_size:
            return self._select(node.left, k)
        elif k > left_size:
            return self._select(node.right, k - left_size - 1)
        else:
            return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def keys(self, lo=None, hi=None):
        result = []
        if lo is None and hi is None:
            lo, hi = self.min(), self.max()
        self._keys(self.root, lo, hi, result)
        return result

    def _keys(self, node, lo, hi, result):
        if node is None:
            return
        if lo < node.key:
            self._keys(node.left, lo, hi, result)
        if lo <= node.key <= hi:
            result.append(node.key)
        if hi > node.key:
            self._keys(node.right, lo, hi, result)

    def size_range(self, lo, hi):
        return len(self.keys(lo, hi))

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def level_order(self):
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def delete_min(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete_max(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        self.root = self._delete_max(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left
        node.right = self._delete_max(node.right)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            temp = node
            node = self._min(temp.right)
            node.right = self._delete_min(temp.right)
            node.left = temp.left
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node