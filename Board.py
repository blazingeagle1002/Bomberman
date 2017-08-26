class Board:
    def __init__(self):
        self.height = 42
        self.width = 92
        self.board = [[' ' for x in range(self.width)]
                      for y in range(self.height)]
        self.__bounds()

    def __bounds(self):
        for x in range(self.height):
            if x < 2:
                for y in range(self.width):
                    self.board[x][y] = 'X'
            elif x > (self.height - 3):
                for y in range(self.width):
                    self.board[x][y] = 'X'
            else:
                self.board[x][0] = 'X'
                self.board[x][1] = 'X'
                self.board[x][2] = 'X'
                self.board[x][3] = 'X'
                self.board[x][self.width - 1] = 'X'
                self.board[x][self.width - 2] = 'X'
                self.board[x][self.width - 3] = 'X'
                self.board[x][self.width - 4] = 'X'

    def border(self):
        for x in range(2, self.height - 2):
            for y in range(4, self.width - 4):
                if self.board[x][y] == 'B':
                    self.board[x][y] = ' '
                elif self.board[x][y] == 'E':
                    self.board[x][y] = ' '
