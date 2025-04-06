# Define the Node class used by both BinaryTree and BinarySearchTree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BinaryTree with methods: levelOrder, isComplete, countLeaves, and pathSum.
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # 1. Level Order Traversal: returns list of lists of node values per level.
    def levelOrder(self):
        result = []
        if self.root is None:
            return result
        
        queue = [self.root]
        while queue:
            size = len(queue)
            lst = []
            for i in range(size):
                current = queue.pop(0)
                lst.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(lst)
        return result
        


    # 2. Check Completeness: returns True if the tree is complete.
    def isComplete(self):
        if self.root is None:
            return True

        queue = [self.root]
        end = False 
        while queue:
            current = queue.pop(0)

            if current.left:
                if end: 
                    return False
                queue.append(current.left)
            else:
                end = True  
            if current.right:
                if end:  
                    return False
                queue.append(current.right)
            else:
                end = True  
        return True


    # 3. Count Leaf Nodes: returns the number of leaf nodes.
    def countLeaves(self):
        count = 0
        if self.root == None:
            return 0
        return self._countLeaves(self.root)

    def _countLeaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._countLeaves(node.left) + self._countLeaves(node.right)
        

    # 4. Root-to-Leaf Path Sum: returns True if a root-to-leaf path equals target sum.
    def pathSum(self, target):
        def _pathsum(root, s):
            if root is None:
                return False
            
            s += root.val
            if root.left is None and root.right is None and s == target:
                return True
            
            return _pathsum(root.left, s) or _pathsum(root.right, s)
        return _pathsum(self.root, 0)
        


# BinarySearchTree (inherits from BinaryTree) with methods: validateBST, rangeSearch, balance.
class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    # 5. Validate BST: returns True if the tree satisfies BST properties.
    def validateBST(self):
        def dfs(root):
            if root is None:
                return True
            if not dfs(root.left):
                return False
            nonlocal prevs
            if prevs >= root.val:
                return False
            prevs = root.val
            return dfs(root.right)
        prevs = float('-inf')
        return dfs(self.root)
        # Todo

    # 6. Range Search: returns a sorted list of node values within [low, high].
    def rangeSearch(self, low, high):
        result = []
        if low is None and high is None:
            low, high = self.min(), self.max()
        self._rangeSearch(self.root, low, high, result)
        return result
    
    def _rangeSearch(self, node, lo, hi, result):
        if node is None:
            return
        if lo < node.val:
            self._rangeSearch(node.left, lo, hi, result)
        if lo <= node.val <= hi:
            result.append(node.val)
        if hi > node.val:
            self._rangeSearch(node.right, lo, hi, result)
        # Todo

    # 7. Balance BST: rebuilds the tree so that it is balanced.
    def balance(self):
        def inorderTraversal(node):
            if node is None:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

        def buildBalancedTree(nodes, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = Node(nodes[mid])
            root.left = buildBalancedTree(nodes, start, mid - 1)
            root.right = buildBalancedTree(nodes, mid + 1, end)
            return root

        nodes = inorderTraversal(self.root)
        self.root = buildBalancedTree(nodes, 0, len(nodes) - 1)
        # Todo
