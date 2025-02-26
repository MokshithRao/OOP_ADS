from typing import Generic, TypeVar, List, Optional, Collection

T = TypeVar('T')

class ArrayListADT(Generic[T]):
    def __init__(self, initial_capacity: int = 10) -> None:
        self._data: List[Optional[T]] = [None] * initial_capacity
        self._size: int = 0
        # print(self._data)

    def size(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        new_data: List[Optional[T]] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        

    def ensure_capacity(self, min_capacity: int) -> None:
        if len(self._data) < min_capacity:
            self._resize(min_capacity)

    def trim_to_size(self) -> None:
        self._resize(self._size)

    def add(self, e: T) -> bool:
        # print(self._data)
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        self._data[self._size] = e
        self._size += 1
       
        return True


    def add_at(self, index: int, element: T) -> None:
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = element
        self._size += 1
        

    def add_all(self, collection: Collection[T]) -> bool:
        for i in collection:
            self.add(i)
        return True

    def add_all_at(self, index: int, collection: Collection[T]) -> bool:
        for i in range(len(collection)):
            self.add_at(index + i, collection[i])
        return True

    def get(self, index: int) -> T:
        return self._data[index]
        # l = []
        # for i in range(len(self._data)):
        #     if self._data[i] != None:
        #         l.append(self._data[i])

        # self._size = len(l)
        # self._data = l
        # return l[index]

    def set(self, index: int, element: T) -> T:
        old_ele = self._data[index]
        self._data[index] = element
        return old_ele

    def remove_at(self, index: int) -> T:
        l = []
        ind = self._data[index]
        for i in range(len(self._data)):
            if i != index:
                l.append(self._data[i])

        self._data = l
        self._size = len(self._data)
        return ind


    def remove(self, o: T) -> bool:
        self._data.remove(o)
        self._size = len(self._data)
        return True

    def clear(self) -> None:
        self._data = []
        self._size = 0

    def contains(self, o: T) -> bool:
        for i in self._data:
            if i == o:
                return True
        return False

    def index_of(self, o: T) -> int:
        for i in range(len(self._data)):
            if self._data[i] == o:
                return i
        return -1

    def last_index_of(self, o: T) -> int:
        l = []
        for i in range(len(self._data)):
            if self._data[i] == o:
                l.append(i)
        return l[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    

    def __str__(self) -> str:
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"








