import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.sum = value

class AVLIndex:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_sum(self, node):
        if not node:
            return 0
        return node.sum

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_node(self, node):
        if not node:
            return
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.sum = node.value + self._get_sum(node.left) + self._get_sum(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_node(y)
        self._update_node(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_node(x)
        self._update_node(y)
        return y

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _insert_rec(self, node, key, value):
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert_rec(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key, value)
        else:
            node.value = value
            self._update_node(node)
            return node

        self._update_node(node)
        balance = self._get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance < -1:
            if key > node.right.key:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _delete_rec(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = self._delete_rec(node.right, temp.key)

        if node is None:
             return node

        self._update_node(node)
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _range_query_rec(self, node, low, high, result):
        if not node:
            return

        if node.key > low:
            self._range_query_rec(node.left, low, high, result)

        if low <= node.key <= high:
            result.append((node.key, node.value))

        if node.key < high:
            self._range_query_rec(node.right, low, high, result)

    def _get_sum_up_to(self, node, k):
        if not node:
            return 0
        if node.key == k:
            return node.value + self._get_sum(node.left)
        elif node.key < k:
            return node.value + self._get_sum(node.left) + self._get_sum_up_to(node.right, k)
        else:
            return self._get_sum_up_to(node.left, k)

    def insert(self, key, value):
        self.root = self._insert_rec(self.root, key, value)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def range_query(self, low, high):
        result = []
        self._range_query_rec(self.root, low, high, result)
        return result

    def aggregate_query(self, low, high):
        sum_high = self._get_sum_up_to(self.root, high)
        sum_low_minus_1 = self._get_sum_up_to(self.root, low - 1)
        return sum_high - sum_low_minus_1

def main():
    num_test_blocks = int(sys.stdin.readline())

    for i in range(num_test_blocks):
        index = AVLIndex()

        num_ops_in_block = int(sys.stdin.readline())

        if i > 0:
            print()

        for _ in range(num_ops_in_block):
            line = sys.stdin.readline().split()
            operation = line[0]
            try:
                args = [int(x) for x in line[1:]]
            except ValueError:
                print(f"Error parsing line: {' '.join(line)}", file=sys.stderr)
                continue

            if operation == 'I':
                if len(args) == 2:
                    key, value = args
                    index.insert(key, value)
                else:
                     print(f"Error: Insert expects 2 arguments", file=sys.stderr)
            elif operation == 'D':
                 if len(args) == 1:
                    key = args[0]
                    index.delete(key)
                 else:
                     print(f"Error: Delete expects 1 argument", file=sys.stderr)
            elif operation == 'R':
                 if len(args) == 2:
                    low, high = args
                    results = index.range_query(low, high)
                    if not results:
                        print("EMPTY")
                    else:
                        print(*(f"{k}:{v}" for k, v in results))
                 else:
                     print(f"Error: Range Query expects 2 arguments", file=sys.stderr)
            elif operation == 'A':
                if len(args) == 2:
                    low, high = args
                    total_sum = index.aggregate_query(low, high)
                    print(total_sum)
                else:
                    print(f"Error: Aggregate Query expects 2 arguments", file=sys.stderr)
            else:
                 print(f"Error: Unknown operation '{operation}'", file=sys.stderr)

if __name__ == "__main__":
    main()