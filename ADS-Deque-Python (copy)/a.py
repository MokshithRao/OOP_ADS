class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return 'true'
        return "false"

    def size(self):
        return self._size

    def add_first(self, item):
        if item is None:
            raise ValueError("Null item not allowed")
        
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def add_last(self, item):
        if item is None:
            raise ValueError("Null item not allowed")
        
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return data

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            data = self.tail.data
            self.tail = current
            self.tail.next = None
        self._size -= 1
        return data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        if self._size == 0:
            return "Steque is empty"

        Current = self.head
        l = []
        while Current:
            l.append(f"{str(Current.data)}")
            Current = Current.next
        return ", ".join(l)

    def main(self):
        while True:
            try:
                s = input()
                if s == "":
                    break
                s = s.split()
                if s[0] == 'isEmpty()':
                    print(self.is_empty())
                elif s[0] == 'Deque()':
                    self.__init__()
                elif s[0] == 'addLast()':
                    self.add_last(s[1])
                elif s[0] == 'addFirst()':
                    self.add_first(s[1])
                elif s[0] == 'removeFirst()':
                    print(self.remove_first())
                elif s[0] == 'removeLast()':
                    print(self.remove_last())
                elif s[0] == 'toString()':
                    print(self.__str__())
                elif s[0] == "size()":
                    print(self.size())
            except Exception as e:
                print("Error:", e)
                break

if __name__ == "__main__":
    deque = Deque()
    deque.main()
