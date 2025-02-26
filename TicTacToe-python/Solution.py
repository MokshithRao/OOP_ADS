class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.grid = []

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.grid.append(row)


    def display(self):
        for i in range(len(self.grid)):
            row = self.grid[i]
            print(" | ".join(row))
        print()


    def is_valid_move(self, row, col):
        if row >= 0 and row < self.size and col >= 0 and col < self.size:
            if self.grid[row][col] == ' ':
                return True
        return False
    

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False


    def check_win(self, symbol):
        for i in range(self.size):
            row_win = True
            col_win = True
            for j in range(self.size):
                if self.grid[i][j] != symbol:
                    row_win = False
                if self.grid[j][i] != symbol:
                    col_win = False
            if row_win or col_win:
                return True

        diag1_win = True
        diag2_win = True
        for i in range(self.size):
            if self.grid[i][i] != symbol:
                diag1_win = False
            if self.grid[i][self.size - 1 - i] != symbol:
                diag2_win = False
        if diag1_win or diag2_win:
            return True
        return False

    def check_draw(self):
        for i in range(len(self.grid)):
            row = self.grid[i]
            for j in range(len(row)):
                if row[j] == ' ':
                    return False
        return True


class Player:
    def __init__(self, symbol, name) -> None:
        self.symbol = symbol
        self.name = name

    def get_move(self, board):
        while True:
            try:
                # row = int(input(f"{self.name} ({self.symbol}), enter row: "))
                # col = int(input(f"{self.name} ({self.symbol}), enter column: "))
                move = input(f"{self.name} ({self.symbol}), enter row and column: ")
                row, col = map(int, move.split())
                if board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number.")





class Game:
    def __init__(self, size, players):
        self.board = Board(size)
        self.players = players
        self.current_player_index = 0

    def switch_player(self):
        if self.current_player_index == 0:
            self.current_player_index = 1
        else:
            self.current_player_index = 0

    def start(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            row, col = current_player.get_move(self.board)
            self.board.place_move(row, col, current_player.symbol)

            if self.board.check_win(current_player.symbol):
                self.board.display()
                print(f"{current_player.name} ({current_player.symbol}) wins!")
                break

            if self.board.check_draw():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()