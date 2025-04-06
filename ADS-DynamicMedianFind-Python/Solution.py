import sys

class BinaryHeap:
    def __init__(self, cmp):
        # Index 0 is unused for simpler arithmetic.
        self.pq = [None]
        self.cmp = cmp  # comparator: returns True if first argument has higher priority than second

    def __len__(self):
        return len(self.pq) - 1

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Heap underflow")
        return self.pq[1]

    def insert(self, x):
        self.pq.append(x)
        self.swim(len(self))

    def del_top(self):
        if self.is_empty():
            raise Exception("Heap underflow")
        top = self.pq[1]
        self.pq[1] = self.pq[-1]
        self.pq.pop()
        if not self.is_empty():
            self.sink(1)
        return top

    def swim(self, k):
        while k > 1 and self.cmp(self.pq[k], self.pq[k // 2]):
            self.pq[k], self.pq[k // 2] = self.pq[k // 2], self.pq[k]
            k //= 2

    def sink(self, k):
        n = len(self)
        while 2 * k <= n:
            j = 2 * k
            if j < n and self.cmp(self.pq[j + 1], self.pq[j]):
                j += 1
            if not self.cmp(self.pq[j], self.pq[k]):
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

class MinPQ(BinaryHeap):
    def __init__(self):
        # For a min-heap, the comparator returns True if x < y.
        super().__init__(lambda x, y: x < y)

    def delMin(self):
        return self.del_top()

class MaxPQ(BinaryHeap):
    def __init__(self):
        # For a max-heap, the comparator returns True if x > y.
        super().__init__(lambda x, y: x > y)

    def delMax(self):
        return self.del_top()

class DynamicMedianFinder:
    def __init__(self):
        # maxHeap stores the lower half and minHeap the upper half of numbers.
        self.maxHeap = MaxPQ()
        self.minHeap = MinPQ()

    def insert(self, x):
        # Insert into maxHeap if empty or x is less than or equal to current median.
        if self.maxHeap.is_empty() or x <= self.maxHeap.peek():
            self.maxHeap.insert(x)
        else:
            self.minHeap.insert(x)

        # Rebalance: maxHeap should have equal or one more element than minHeap.
        if len(self.maxHeap) > len(self.minHeap) + 1:
            self.minHeap.insert(self.maxHeap.delMax())
        elif len(self.maxHeap) < len(self.minHeap):
            self.maxHeap.insert(self.minHeap.delMin())

    def getMedian(self):
        if self.maxHeap.is_empty():
            return "Invalid"
        return str(self.maxHeap.peek())

    def removeMedian(self):
        if self.maxHeap.is_empty():
            return "Invalid"
        median = self.maxHeap.delMax()
        if len(self.maxHeap) < len(self.minHeap):
            self.maxHeap.insert(self.minHeap.delMin())
        return str(median)

def main():
    input_lines = sys.stdin.read().strip().splitlines()
    dm = DynamicMedianFinder()
    output_lines = []

    for line in input_lines:
        if not line.strip():
            continue
        parts = line.split()
        op = parts[0]
        if op == "I":
            dm.insert(int(parts[1]))
        elif op == "M":
            output_lines.append(dm.getMedian())
        elif op == "R":
            output_lines.append(dm.removeMedian())

    print("\n".join(output_lines))

if __name__ == '__main__':
    main()
