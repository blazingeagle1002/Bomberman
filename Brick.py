from random import randint


class Brick:
    def __init__(self, board):
        self.__align_bricks(board)
        self.cnt = 60

    def __align_bricks(self, board):
        val = 0
        while(val != 60):
            x = randint(2, 89)
            y = randint(4, 37)
            if(board.board[y][x] == ' ') \
                and (board.board[y + 1][x] == ' ') \
                and (board.board[y][x + 3] == ' ') \
                    and (board.board[y + 1][x + 3] == ' '):
                if (x % 4 == 0) and (y % 2 == 0):
                    val += 1
                    for i in range(0, 2):
                        for j in range(0, 4):
                            board.board[y + i][x + j] = '\\'
