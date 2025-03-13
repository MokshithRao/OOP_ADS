class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
    
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
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
        


    def add_last(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1


    def remove_first(self):
        if not self.head:
             raise IndexError("Deque is empty")
        
        removed_data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return removed_data

    
    def remove_last(self):
        if not self.head:
             raise IndexError("Deque is empty")
        
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        else:
            Current = self.head
            while Current.next != self.tail:
                Current = Current.next
            removed_data = self.tail.data
            self.tail = Current
            self.tail.next = None

        self._size -= 1
        return removed_data
    


    def iterator(self):
        Current = self.head
        while Current:
            Current = Current.next
        return Current



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
                    (self.add_last(s[1]))

                elif s[0] == 'addFirst()':
                    (self.add_first(s[1]))

                elif s[0] == 'removeFirst()':
                    print(self.remove_first())
                
                elif s[0] == 'removeLast()':
                    print(self.remove_last())

                elif s[0] == 'iterator()':
                    print(self.iterator())
                
                elif s[0] == 'toString()':
                    print(self.__str__())
                
                elif s[0] == "size()":
                    print(self.size())

            except:
                break


if __name__ == '__main__':
    deque = Deque()
    deque.main()




