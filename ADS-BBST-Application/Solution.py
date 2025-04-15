class Node:
    def __init__(self, key, value, color, left=None, right=None, size=1):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.size = size
        self.sum = value


class RedBlackTree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if not node:
            return False
        return node.color

    def size(self, node):
        if node is None:
            return 0
        return node.size


    def sum_values(self, node):
        if node is None:
            return 0
        return node.sum


    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = True
        x.size = h.size
        x.sum = h.sum
        self.update(h)
        return x



    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = True
        x.size = h.size
        x.sum = h.sum
        self.update(h)
        return x


    def flip_colors(self, h):
        h.color = True
        if h.left:
            h.left.color = False
        if h.right:
            h.right.color = False


    def update(self, h):
        h.size = 1 + self.size(h.left) + self.size(h.right)
        h.sum = h.value + self.sum_values(h.left) + self.sum_values(h.right)



    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = False


    def _insert(self, h, key, value):
        if not h:
            return Node(key, value, True)

        if key < h.key:
            h.left = self._insert(h.left, key, value)
        elif key > h.key:
            h.right = self._insert(h.right, key, value)
        else:
            h.value = value

        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)

        self.update(h)
        return h


    def delete(self, key):
        self.root = self._delete(self.root, key)
        if self.root:
            self.root.color = False


    def _delete(self, h, key):
        if not h:
            return None

        if key < h.key:
            h.left = self._delete(h.left, key)
        elif key > h.key:
            h.right = self._delete(h.right, key)
        else:
            if not h.right:
                return h.left
            if not h.left:
                return h.right

            temp = self._min(h.right)
            h.key, h.value = temp.key, temp.value
            h.right = self._delete(h.right, temp.key)

        self.update(h)
        return h


    def _min(self, h):
        while h.left:
            h = h.left
        return h


    def range_query(self, node, low, high, result):
        if not node:
            return
        if low < node.key:
            self.range_query(node.left, low, high, result)
        if low <= node.key <= high:
            result.append((node.key, node.value))
        if node.key < high:
            self.range_query(node.right, low, high, result)



    def range_sum(self, node, low, high):
        if not node:
            return 0
        
        if node.key < low:
            return self.range_sum(node.right, low, high)
        elif node.key > high:
            return self.range_sum(node.left, low, high)
        else:
            return (node.value + self.range_sum(node.left, low, high) + self.range_sum(node.right, low, high))


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    line = 1

    for _ in range(t):
        rbt = RedBlackTree()
        q = int(data[line])
        line += 1

        for _ in range(q):
            s = data[line].split()
            line += 1

            if s[0] == "I":
                key = int(s[1])
                val = int(s[2])
                rbt.insert(key, val)

            elif s[0] == "D":
                key = int(s[1])
                rbt.delete(key)

            elif s[0] == "R":
                l = int(s[1])
                h = int(s[2])
                result = []
                rbt.range_query(rbt.root, l, h, result)
                if result:
                    result.sort()
                    print(" ".join(f"{k}:{v}" for k, v in result))
                else:
                    print("EMPTY")

            elif s[0] == "A":
                l = int(s[1])
                h = int(s[2])
                print(rbt.range_sum(rbt.root, l, h))
        print()

if __name__ == "__main__":
    main()
