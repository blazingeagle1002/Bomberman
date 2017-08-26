class walls:
    def __init__(self, board):
        self.__wall(board)

    def __wall(self, board):
        for y in range(2, board.height - 2):
            if (y % 4 == 0) or (y % 4 == 1):
                for x in range(4, board.width - 4):
                    if (x % 8 == 0) or (x % 8 == 1) \
                    		or (x % 8 == 2) or (x % 8 == 3):
                        board.board[y][x] = 'X'
