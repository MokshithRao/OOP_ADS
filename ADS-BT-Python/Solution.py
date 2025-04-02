class BinaryTree:
    class BTNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.data)

    def __init__(self, element=None, left_tree=None, right_tree=None):
        # When element is None, we create an empty tree.
        if element is None:
            self.root = None
        else:
            self.root = BinaryTree.BTNode(element)
            if left_tree is not None:
                self.root.left = left_tree.root
            if right_tree is not None:
                self.root.right = right_tree.root

    def countInternal(self):
        """Returns the number of internal (non-leaf) nodes in the tree."""
        if self.root is None:
            return 0
        
        stack = [self.root]
        count = 0
        
        while stack:
            node = stack.pop()
            if node.left or node.right:
                count += 1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return count



    def height(self):
        """Returns the height of the tree.
        Height is defined as the number of nodes on the longest path from the root down to a leaf.
        """
        if self.root is None:
            return 0
        
        stack = [(self.root, 1)]
        max_height = 0
        
        while stack:
            node, depth = stack.pop()
            max_height = max(max_height, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_height



    def isPerfect(self):
        """Returns True if the tree is perfect.
        A perfect tree is one in which every internal node has two children and all leaves are at the same depth.
        """
        if self.root is None:
            return True
        
        queue = [(self.root, 0)]
        level_nodes = {}
        
        while queue:
            node, level = queue.pop(0)
            if level not in level_nodes:
                level_nodes[level] = 0
            level_nodes[level] += 1
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        depth = max(level_nodes.keys())
        for i in range(depth):
            if level_nodes[i] != 2 ** i:
                return False
        
        return level_nodes[depth] == 2 ** depth


    def __str__(self):
        lines = []
        self._preOrderTraversal(self.root, 0, lines)
        return "\n".join(lines)

    def _preOrderTraversal(self, node, depth, lines):
        indent = "  " * (depth - 1) if depth > 0 else ""
        if node is None:
            lines.append(indent + "null")
        else:
            lines.append(indent + str(node))
            self._preOrderTraversal(node.left, depth + 1, lines)
            self._preOrderTraversal(node.right, depth + 1, lines)

