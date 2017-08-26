from Person import person
import time


class bomberman(person):
    def __init__(self):
        self.lives = 3
        self.x = 2
        self.y = 4
        self.score = 0

    def position(self, board):
        if board.board[self.x][self.y] == ' ':
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.x + i][self.y + j] = 'B'

    def move(self, board, val):
        if val == 'a':
            if (board.board[self.x][self.y - 4] == ' ' and
                    board.board[self.x + 1][self.y - 4] == ' '):
                self.y -= 4
                time.sleep(0.3)
            if (board.board[self.x][self.y - 4] == 'e' and
                    board.board[self.x + 1][self.y - 4] == 'e'):
                self.lives -= 1
        elif val == 'd':
            if (board.board[self.x][self.y + 7] == ' ' and
                    board.board[self.x + 1][self.y + 7] == ' '):
                self.y += 4
                time.sleep(0.3)
            if (board.board[self.x][self.y + 7] == 'e' and
                    board.board[self.x + 1][self.y + 7] == 'e'):
                self.lives -= 1
        elif val == 'w':
            if (board.board[self.x - 2][self.y] == ' ' and
                    board.board[self.x - 2][self.y + 3] == ' '):
                self.x -= 2
                time.sleep(0.3)
            if (board.board[self.x - 2][self.y] == 'e' and
                    board.board[self.x - 2][self.y + 3] == 'e'):
                self.lives -= 1
        elif val == 's':
            if (board.board[self.x + 3][self.y] == ' ' and
                    board.board[self.x + 3][self.y + 3] == ' '):
                self.x += 2
                time.sleep(0.3)
            if (board.board[self.x + 3][self.y] == 'e' and
                    board.board[self.x + 3][self.y + 3] == 'e'):
                self.lives -= 1

    def get_life(self):
        return self.lives
