class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        # For a simple representation
        return str(self.data)


# 1. copy: Return a deep copy of the tree.
def copy_tree(t):
    if t is None:
        return None
    return BTNode(t.data, copy_tree(t.left), copy_tree(t.right))

# 2. replace: Replace all occurrences of old_value with new_value.
#    Return the count of nodes replaced.
def replace(t, old_value, new_value):
    if t is None:
        return 0
    count = 0
    if t.data == old_value:
        t.data = new_value
        count = 1
    return count + replace(t.left, old_value, new_value) + replace(t.right, old_value, new_value)


# 3. countNodesAtDepth: Count the number of nodes at the given depth.
def countNodesAtDepth(t, depth):
    if t is None:
        return 0
    if depth == 0:
        return 1
    return countNodesAtDepth(t.left, depth - 1) + countNodesAtDepth(t.right, depth - 1)



# 4. allSame: Return True if every value in the tree is the same.
def allSame(t):
    if t is None:
        return True
    value = t.data
    def check(node):
        if node is None:
            return True
        if node.data != value:
            return False
        return check(node.left) and check(node.right)
    return check(t)


# 5. leafList: Return a list of the data values in the leaves of the tree.
def leafList(t):
    if t is None:
        return []
    if t.left is None and t.right is None:
        return [t.data]
    return leafList(t.left) + leafList(t.right)


# 6. reflect: Modify the tree so that it is reflected horizontally.
def reflect(t):
    if t is None:
        return
    t.left, t.right = t.right, t.left
    reflect(t.left)
    reflect(t.right)


# 7. condense: Remove nodes with exactly one child.
def condense(t):
    if t is None:
        return None
    t.left = condense(t.left)
    t.right = condense(t.right)
    
    if t.left is None and t.right is not None:
        return t.right
    if t.right is None and t.left is not None:
        return t.left
    return t


# Function to perform pre-order traversal of the tree.
def print_preorder(t):
    if t is None:
        return
    print(t.data, end=" ")
    print_preorder(t.left)
    print_preorder(t.right)



