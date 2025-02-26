class Clock:
    def __init__(self, *time) -> None:
        # print(len(time), time)
        if len(time) == 2:
            # print("a")
            if time[0] > 24 or time[0] < 0 or time[1] > 60 or time[1] <= 0:
                self.hrs = 0
                self.min = 0
            else:
                self.hrs = time[0]
                self.min = time[1]
                
        if len(time) == 1:
            time = time[0].split(":")
            if int(time[0]) > 24 or int(time[0]) < 0 or int(time[1]) > 60 or int(time[1]) <= 0:
                self.hrs = 0
                self.min = 0
            else:
                self.hrs = int(time[0])
                self.min = int(time[1])


    def tic(self):
        self.min +=1 
        if self.min == 60:
            self.min = 0
            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0


    def toc(self, minutes):
        self.min += minutes
        while self.min >= 60:
            self.min -= 60

            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0


    def isEarlierThan(self, clock):
        if self.hrs < clock.hrs:
            return True
        elif self.hrs == clock.hrs and self.min < clock.min:
            return True
        return False


    def toString(self) -> str:
        return f"{self.hrs:02d}:{self.min:02d}"


# c = Clock()

con1 = input()
con2 = input()

con2 = int(con2)
while con2 > 0:
    # print("b")
    # print()
    if con1 == 'constructor(int, int)':
        s = input().split(',')
        # print("aaa")
        # print(s[0],s[1])
        a = Clock(int(s[0]), int(s[1]))
        print(a.toString())

    elif con1 == 'constructor(String)':
        s = input()
        a = Clock(s)
        print(a.toString())

    elif con1 == 'tic()':
        s = input()
        a = Clock(s)
        a.tic()
        print(a.toString())

    elif con1 == 'toc(int)':
        s = input().split(',')
        a = Clock(s[0])
        a.toc(int(s[1]))
        print(a.toString())

    elif con1 == 'isEarlierThan(Clock)':
        s = input().split(',')
        a1 = Clock(s[0])
        a2 = Clock(s[1])
        if a1.isEarlierThan(a2):
            print('true')
        else:
            print('false')

    elif con1 == "toString()":
        print('null')


    con2 -= 1


