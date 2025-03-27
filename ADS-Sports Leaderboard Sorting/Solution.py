from functools import cmp_to_key

class Scorecard:
    def __init__(self,team_name, wins, losses, draws, no_result, points):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.no_result = no_result
        self.points = points
    
    def __str__(self):
        return f"{self.team_name}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.no_result}"
    
    def compare(self, other):
        if self.points < other.points:
            return 1
        elif self.points > other.points:
            return -1
        else:
            if self.wins < other.wins:
                return 1
            elif self.wins > other.wins:
                return -1
            else:
                if self.losses < other.losses:
                    return -1
                elif self.losses > other.losses:
                    return 1
                else:
                    if self.draws < other.draws:
                        return 1
                    elif self.draws > other.draws:
                        return -1
                    else:
                        if self.no_result < other.no_result:
                            return -1
                        elif self.no_result > other.no_result:
                            return 1
                        else:
                            if self.team_name < other.team_name:
                                return -1
                            elif self.team_name < other.team_name:
                                return 1
        return 0

    
class BinaryHeapPriorityQueue:
    def __init__(self):
        self.arr = []
        self.size_ = 0

    def add(self, e):
        self.arr.append(e)
        self.size_ += 1
        self.swim(self.size_ - 1)
    
    def offer(self, e):
        self.add(e)
    

    def size(self):
        return self.size_
    
    def contains(self, e):
        for i in self.arr:
            if i == e:
                return True
        return False
    
    def index_of(self, e):
        for i in range(len(self.arr)):
            if self.arr[i] == e:
                return i
        return None
    
    def peek(self):
        return self.arr[0]
    
    def poll(self):        
        root = self.arr[0]
        self.arr[0] = self.arr[self.size_ - 1]
        self.size_ -= 1
        self.arr.pop()
        self.sink(0)
        return root
    
    def remove(self, e):
        index = self.index_of(e)        
        self.arr[index] = self.arr[self.size_ - 1]
        self.size_ -= 1
        self.arr.pop()
        self.sink(index)
        self.swim(index)
        return True
    
    def clear(self):
        self.arr = []
        self.size_ = 0

    def iterator(self):
        return self.arr
    
    def __str__(self):
        return f"{self.arr}"

    def swim(self, index):
        while index > 0 :
            parent = (index-1)//2
            if Scorecard.compare(self.arr[index], self.arr[parent]) < 0:
                self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
                index = parent
            else:
                break
    
    def sink(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        s = index
        
        if left < self.size_ and Scorecard.compare(self.arr[left], self.arr[s]) < 0:
            s = left
        
        if right < self.size_ and Scorecard.compare(self.arr[right], self.arr[s]) < 0:
            s = right
        
        if s != index:
            self.arr[index], self.arr[s] = self.arr[s], self.arr[index]
            self.sink(s)







def sort():
    team_data = []
    x = 0
    while True:
        try:
            s = input().split(",")
            if len(s) == 1:
                x = int(s[0])
            elif len(s) > 1:
                team = Scorecard(s[0], int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5]))
                team_data.append(team)

        except Exception as e:
            break

    PQ = BinaryHeapPriorityQueue()
    for team in team_data:
        PQ.add(team)
    
    print(f"Top {x} teams:")
    for i in range(x):
        print(PQ.poll())

sort()