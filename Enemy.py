from Person import person
from random import randint


class Enemy(person):
    def __init__(self, board):
        self.__position(board)
        self.life = 1

    def __position(self, board):
        val = 0
        while(val != 1):
            x = randint(2, 89)
            y = randint(4, 37)
            if(board.board[y][x] == ' ') and (board.board[y + 1][x] == ' '):
                if (board.board[y][x + 3] == ' ') \
                		and (board.board[y + 1][x + 3] == ' '):
                    if (x % 4 == 0) and (y % 2 == 0):
                        val = 1
                        self.x = x
                        self.y = y

    def pos(self, board):
        for i in range(0, 2):
            for j in range(0, 4):
                if(board.board[self.y + i][self.x + j] != 'e'):
                    board.board[self.y + i][self.x + j] = 'E'

    def move(self, board):
        while (1):
            ranx = randint(1, 4)
            if ranx == 1:
                if ((board.board[self.y][self.x - 4] == ' ') and
                        (board.board[self.y + 1][self.x - 4] == ' ')):
                    self.x -= 4
                    return 0
                elif ((board.board[self.y][self.x - 4] == 'B') and
                        (board.board[self.y + 1][self.x - 4] == 'B')):
                    self.x -= 4
                    return 1
                elif ((board.board[self.y][self.x - 4] == 'e') and
                        (board.board[self.y + 1][self.x - 4] == 'e')):
                    self.x -= 4
                    self.life = 0

            if ranx == 2:
                if ((board.board[self.y][self.x + 7] == ' ') and
                        (board.board[self.y + 1][self.x + 7] == ' ')):
                    self.x += 4
                    return 0
                elif ((board.board[self.y][self.x + 7] == 'B') and
                        (board.board[self.y + 1][self.x + 7] == 'B')):
                    self.x += 4
                    return 1
                elif ((board.board[self.y][self.x + 7] == 'e') and
                        (board.board[self.y + 1][self.x + 7] == 'e')):
                    self.x += 4
                    self.life = 0

            if ranx == 3:
                if ((board.board[self.y - 2][self.x] == ' ') and
                        (board.board[self.y - 2][self.x + 3] == ' ')):
                    self.y -= 2
                    return 0
                elif ((board.board[self.y - 2][self.x] == 'B') and
                        (board.board[self.y - 2][self.x + 3] == 'B')):
                    self.y -= 2
                    return 1
                elif ((board.board[self.y - 2][self.x] == 'e') and
                        (board.board[self.y - 2][self.x + 3] == 'e')):
                    self.y -= 2
                    self.life = 0

            if ranx == 4:
                if ((board.board[self.y + 3][self.x] == ' ') and
                        (board.board[self.y + 3][self.x + 3] == ' ')):
                    self.y += 2
                    return 0
                elif ((board.board[self.y + 3][self.x] == 'B') and
                        (board.board[self.y + 3][self.x + 3] == 'B')):
                    self.y += 2
                    return 1
                elif ((board.board[self.y + 3][self.x] == 'e') and
                        (board.board[self.y + 3][self.x + 3] == 'e')):
                    self.y += 2
                    self.life = 0
