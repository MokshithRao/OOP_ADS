class BingoBoard:
    size = 5

    def __init__(self, board):
        self.board = board
        self.marks = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(False)
            self.marks.append(row)

    def markNumbers(self, calledNumbers):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(len(calledNumbers)):
                    # print(self.board[i][j])
                    if self.board[i][j] == calledNumbers[k]:
                        self.marks[i][j] = True

    def isRowComplete(self, row):
        for j in range(self.size):
            # print(self.marks[row][j])
            if not self.marks[row][j]:
                return False
        return True

    def isColumnComplete(self, column):
        for i in range(self.size):
            if not self.marks[i][column]:
                return False
        return True

    def isMainDiagonalComplete(self):
        for i in range(self.size):
            if not self.marks[i][i]:
                return False
        return True

    def isAntiDiagonalComplete(self):
        for i in range(self.size):
            # print("sddfgd")
            if not self.marks[i][self.size - 1 - i]:
                return False
        return True

    def printBoard(self):
        for i in range(self.size):
            r = ""
            for j in range(self.size):
                # print('aaaaaaa')
                if self.marks[i][j]:
                    r+="X  "
                    # print(r.strip())
                else:
                    r+=str(self.board[i][j])+"  "
            print(r.strip())
            # print()

class BingoGame:
    letters = ["B", "I", "N", "G", "O"]

    def __init__(self, board, calledNumbers):
        self.board = board
        self.calledNumbers = calledNumbers
        self.bingoLetters = []

    def play(self):
        self.board.markNumbers(self.calledNumbers)
        completed_lines = 0
        
        for i in range(BingoBoard.size):
            if self.board.isRowComplete(i):
                # print('aaaaa')
                completed_lines += 1
            if self.board.isColumnComplete(i):
                completed_lines += 1

        if self.board.isMainDiagonalComplete():
            completed_lines += 1
        if self.board.isAntiDiagonalComplete():
            completed_lines += 1

        # m = min(completed_lines, len(self.letters) - len(self.bingoLetters))
        for i in range(min(completed_lines, len(self.letters) - len(self.bingoLetters))):
            self.bingoLetters.append(self.letters[len(self.bingoLetters)])
        
        self.board.printBoard()
        self.printResult()

    def printResult(self):
        if len(self.bingoLetters) == len(self.letters):
            print()
            print(" ".join(self.bingoLetters))
            print("Game Completed!")
        else:
            remaining_letters = " ".join(self.letters[len(self.bingoLetters):])
            print()
            print("Remaining Letters:", remaining_letters)


def main():
    board_numbers = []
    for i in range(5):
        row = input().split()
        row_numbers = []
        for num in row:
            # print(num)
            row_numbers.append(int(num))
        board_numbers.append(row_numbers)
    
    called_numbers = input().split(',')
    # print(called_numbers)
    called_numbers_list = []
    for num in called_numbers:
        called_numbers_list.append(int(num))
    
    board = BingoBoard(board_numbers)
    game = BingoGame(board, called_numbers_list)
    game.play()


if __name__ == "__main__":
    main()


