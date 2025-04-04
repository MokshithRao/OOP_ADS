class Node:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, data):
        self.root = self._add_recursive(self.root, data)

    def _add_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._add_recursive(node.left, data)
        elif data > node.data:
            node.right = self._add_recursive(node.right, data)
        return node


    def contains(self, data):
        return self._contains_recursive(self.root, data)
    
    def _contains_recursive(self, node, data):
        if node is None:
            return False
        if data < node.data:
            return self._contains_recursive(node.left, data)
        elif data > node.data:
            return self._contains_recursive(node.right, data)
        return True

    def max(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def size(self):
        return self._size_recursive(self.root)
    

    def _size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def in_order(self):
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)

    def pre_order(self):
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)


