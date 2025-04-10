class Node:
    def __init__(self, key, value, color, left=None, right=None, size=1):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.size = size


class RedBlackBST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = 0

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, 1)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        if self._isRed(node.right) and not self._isRed(node.left):
            node = self._rotateLeft(node)
        if self._isRed(node.left) and self._isRed(node.left.left):
            node = self._rotateRight(node)
        if self._isRed(node.left) and self._isRed(node.right):
            self._flipColors(node)

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _isRed(self, node):
        return node is not None and node.color == 1

    def _rotateLeft(self, h):
        temp = h.right
        h.right = temp.left
        temp.left = h
        temp.color = h.color
        h.color = 1
        temp.size = h.size
        h.size = 1 + self._size(h.left) + self._size(h.right)
        return temp

    def _rotateRight(self, h):
        temp = h.left
        h.left = temp.right
        temp.right = h
        temp.color = h.color
        h.color = 1
        temp.size = h.size
        h.size = 1 + self._size(h.left) + self._size(h.right)
        return temp

    def _flipColors(self, h):
        h.color = 1
        h.left.color = 0
        h.right.color = 0

    def _size(self, node):
        return node.size if node else 0

    def isBST(self):
        return self._isBST(self.root, None, None)

    def _isBST(self, node, min_key, max_key):
        if node is None:
            return True
        if (min_key is not None and node.key <= min_key) or (max_key is not None and node.key >= max_key):
            return False
        return self._isBST(node.left, min_key, node.key) and self._isBST(node.right, node.key, max_key)

    def is23(self):
        return self._is23(self.root)

    def _is23(self, node):
        if node is None:
            return True
        if self._isRed(node.right):
            return False
        if self._isRed(node.left) and self._isRed(node.left.left):
            return False
        return self._is23(node.left) and self._is23(node.right)

    def isBalanced(self):
        try:
            black_height = self._blackHeight(self.root)
            return self._isBalanced(self.root, black_height, 0)
        except ValueError:
            return False

    def _blackHeight(self, node):
        if node is None:
            return 0
        left_black = self._blackHeight(node.left)
        right_black = self._blackHeight(node.right)
        if left_black != right_black:
            raise ValueError()
        return left_black + (1 if node.color == 0 else 0)

    def _isBalanced(self, node, total_black, current_black):
        if node is None:
            return current_black == total_black
        if node.color == 0:
            current_black += 1
        return self._isBalanced(node.left, total_black, current_black) and self._isBalanced(node.right, total_black, current_black)

    def isRedBlackBST(self):
        return self.isBST() and self.is23() and self.isBalanced()
