''' This is the bomb'''
from threading import Timer
from Person import Person

class Bomb(Person):
    ''' Brace for impact '''
    def __init__(self):
        super(Bomb, self).__init__()
        self.live = 0
        self.width = 92
        self.height = 42
        self.bomb = [[' ' for _ in range(92)]
                     for _ in range(42)]

    def explode(self, row, col, board, bomber, list_enem):
        ''' Bomb exploded... take shelter'''
        self.live = 0
        for i in range(0, 2):
            for j in range(0, 4):
                self.bomb[self.row + i][self.col + j] = ' '
                board.board[self.row + i][self.col + j] = 'e'

        row = row + 1
        row = row - 1
        col = col + 1
        col = col - 1

        if (board.board[self.row + 2][self.col] != 'X') \
            and (board.board[self.row + 3][self.col] != 'X') \
            and (board.board[self.row + 2][self.col + 3] != 'X') \
                and (board.board[self.row + 3][self.col + 3] != 'X'):
            if (board.board[self.row + 2][self.col] == '\\') \
                and (board.board[self.row + 3][self.col] == '\\') \
                and (board.board[self.row + 2][self.col + 3] == '\\') \
                    and (board.board[self.row + 3][self.col + 3] == '\\'):
                bomber.score += 20
            value = len(list_enem)
            for i in range(value):
                if (self.row + 2 == list_enem[i].col) \
                        and (self.col == list_enem[i].row):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.row + 2 + i][self.col + j] = 'e'

        if (board.board[self.row - 1][self.col] != 'X') \
            and (board.board[self.row - 2][self.col] != 'X') \
            and (board.board[self.row - 1][self.col + 3] != 'X') \
                and (board.board[self.row - 2][self.col + 3] != 'X'):
            if (board.board[self.row - 1][self.col] == '\\') \
                and (board.board[self.row - 2][self.col] == '\\') \
                and (board.board[self.row - 1][self.col + 3] == '\\') \
                    and (board.board[self.row - 2][self.col + 3] == '\\'):
                bomber.score += 20
            value = len(list_enem)
            for i in range(value):
                if (self.row - 2 == list_enem[i].col) \
                        and (self.col == list_enem[i].row):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.row - 2 + i][self.col + j] = 'e'

        if (board.board[self.row][self.col + 4] != 'X') \
            and (board.board[self.row][self.col + 7] != 'X') \
            and (board.board[self.row + 1][self.col + 4] != 'X') \
                and (board.board[self.row + 1][self.col + 7] != 'X'):
            if (board.board[self.row][self.col + 4] == '\\') \
                and (board.board[self.row][self.col + 7] == '\\') \
                and (board.board[self.row + 1][self.col + 4] == '\\') \
                    and (board.board[self.row + 1][self.col + 7] == '\\'):
                bomber.score += 20
            value = len(list_enem)
            for i in range(value):
                if (self.row == list_enem[i].col) \
                        and (self.col + 4 == list_enem[i].row):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.row + i][self.col + 4 + j] = 'e'

        if (board.board[self.row][self.col - 1] != 'X') \
            and (board.board[self.row][self.col - 4] != 'X') \
            and (board.board[self.row + 1][self.col - 1] != 'X') \
                and (board.board[self.row + 1][self.col - 4] != 'X'):
            if (board.board[self.row][self.col - 1] != 'X') \
                and (board.board[self.row][self.col - 4] != 'X') \
                and (board.board[self.row + 1][self.col - 1] != 'X') \
                    and (board.board[self.row + 1][self.col - 4] != 'X'):
                bomber.score += 20
            value = len(list_enem)
            for i in range(value):
                if (self.row == list_enem[i].col) \
                        and (self.col - 4 == list_enem[i].row):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.row + i][self.col - 4 + j] = 'e'

        end = Timer(0.8, self.remove, [self.row, self.col, board])
        end.start()

        if self.row == bomber.row and self.col == bomber.col:
            bomber.lives -= 1
            bomber.row = 2
            bomber.col = 4
            bomber.position(board)
        if (self.row + 2) == bomber.row and self.col == bomber.col:
            bomber.lives -= 1
            bomber.row = 2
            bomber.col = 4
            bomber.position(board)
        if (self.row - 2) == bomber.row and self.col == bomber.col:
            bomber.lives -= 1
            bomber.row = 2
            bomber.col = 4
            bomber.position(board)
        if self.row == bomber.row and (self.col + 4) == bomber.col:
            bomber.lives -= 1
            bomber.row = 2
            bomber.col = 4
            bomber.position(board)
        if self.row == bomber.row and (self.col - 4) == bomber.col:
            bomber.lives -= 1
            bomber.row = 2
            bomber.col = 4
            bomber.position(board)


    def remove(self, row, col, board):
        ''' Remove the bomb '''
        for i in range(0, 2):
            for j in range(0, 4):
                if (board.board[row + 2][col] != 'X') \
                    and (board.board[row + 3][col] != 'X') \
                    and (board.board[row + 2][col + 3] != 'X') \
                        and (board.board[row + 3][col + 3] != 'X'):
                    board.board[self.row + 2 + i][self.col + j] = ' '

                if (board.board[row - 1][col] != 'X') \
                    and (board.board[row - 2][col] != 'X') \
                    and (board.board[row - 1][col + 3] != 'X') \
                        and (board.board[row - 2][col + 3] != 'X'):
                    board.board[self.row - 2 + i][self.col + j] = ' '

                if (board.board[row][col + 4] != 'X') \
                    and (board.board[row][col + 7] != 'X') \
                    and (board.board[row + 1][col + 4] != 'X') \
                        and (board.board[row + 1][col + 7] != 'X'):
                    board.board[self.row + i][self.col + 4 + j] = ' '

                if (board.board[row][col - 1] != 'X') \
                    and (board.board[row][col - 4] != 'X') \
                    and (board.board[row + 1][col - 1] != 'X') \
                        and (board.board[row + 1][col - 4] != 'X'):
                    board.board[self.row + i][self.col - 4 + j] = ' '

                board.board[self.row + i][self.col + j] = ' '

    def pos(self, row, col):
        ''' This is for the position '''
        if self.live == 0:
            for i in range(0, 2):
                for j in range(0, 4):
                    self.bomb[row + i][col + j] = 'O'
            self.row = row
            self.col = col
            self.live = 1
