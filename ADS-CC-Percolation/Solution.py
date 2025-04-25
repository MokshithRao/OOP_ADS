class Percolation:
    def __init__(self, n):
        self.n = n
        self.grid = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            self.grid.append(row)

        self.visited = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            self.visited.append(row)

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 


    def open_site(self, row, col):
        self.grid[row][col] = True

    def dfs(self, row, col):
        stack = []
        stack.append((row, col))

        while len(stack) > 0:
            current = stack.pop()
            r = current[0]
            c = current[1]

            if r < 0 or r >= self.n or c < 0 or c >= self.n:
                continue
            if not self.grid[r][c]:
                continue
            if self.visited[r][c]:
                continue

            self.visited[r][c] = True

            for i in range(len(self.directions)):
                dr = self.directions[i][0]
                dc = self.directions[i][1]
                stack.append((r + dr, c + dc))

    def percolates(self):
        for col in range(self.n):
            if self.grid[0][col] and not self.visited[0][col]:
                self.dfs(0, col)

        for col in range(self.n):
            if self.visited[self.n - 1][col]:
                return True
        return False


def main():
    n = int(input())
    percolation = Percolation(n)

    try:
        while True:
            line = input()
            if line.strip() == "":
                continue
            row_col = line.split()
            row = int(row_col[0]) - 1
            col = int(row_col[1]) - 1
            percolation.open_site(row, col)
    except:
        pass

    if percolation.percolates():
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()
