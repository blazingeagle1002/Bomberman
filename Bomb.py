from Person import person
from threading import Timer


class Bomb(person):
    def __init__(self):
        self.live = 0
        self.width = 92
        self.height = 42
        self.bomb = [[' ' for x in range(92)] for y in range(42)]

    def explode(self, x, y, board, bomber, list_enem):
        self.live = 0
        for i in range(0, 2):
            for j in range(0, 4):
                self.bomb[self.x + i][self.y + j] = ' '
                board.board[self.x + i][self.y + j] = 'e'

        if (board.board[self.x + 2][self.y] != 'X') \
            and (board.board[self.x + 3][self.y] != 'X') \
            and (board.board[self.x + 2][self.y + 3] != 'X') \
                and (board.board[self.x + 3][self.y + 3] != 'X'):
            if (board.board[self.x + 2][self.y] == '\\') \
                and (board.board[self.x + 3][self.y] == '\\') \
                and (board.board[self.x + 2][self.y + 3] == '\\') \
                    and (board.board[self.x + 3][self.y + 3] == '\\'):
                bomber.score += 20
            for i in range(len(list_enem)):
                if (self.x + 2 == list_enem[i].y) \
                        and (self.y == list_enem[i].x):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.x + 2 + i][self.y + j] = 'e'

        if (board.board[self.x - 1][self.y] != 'X') \
            and (board.board[self.x - 2][self.y] != 'X') \
            and (board.board[self.x - 1][self.y + 3] != 'X') \
                and (board.board[self.x - 2][self.y + 3] != 'X'):
            if (board.board[self.x - 1][self.y] == '\\') \
                and (board.board[self.x - 2][self.y] == '\\') \
                and (board.board[self.x - 1][self.y + 3] == '\\') \
                    and (board.board[self.x - 2][self.y + 3] == '\\'):
                bomber.score += 20
            for i in range(len(list_enem)):
                if (self.x - 2 == list_enem[i].y) \
                        and (self.y == list_enem[i].x):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.x - 2 + i][self.y + j] = 'e'

        if (board.board[self.x][self.y + 4] != 'X') \
            and (board.board[self.x][self.y + 7] != 'X') \
            and (board.board[self.x + 1][self.y + 4] != 'X') \
                and (board.board[self.x + 1][self.y + 7] != 'X'):
            if (board.board[self.x][self.y + 4] == '\\') \
                and (board.board[self.x][self.y + 7] == '\\') \
                and (board.board[self.x + 1][self.y + 4] == '\\') \
                    and (board.board[self.x + 1][self.y + 7] == '\\'):
                bomber.score += 20
            for i in range(len(list_enem)):
                if (self.x == list_enem[i].y) \
                        and (self.y + 4 == list_enem[i].x):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.x + i][self.y + 4 + j] = 'e'

        if (board.board[self.x][self.y - 1] != 'X') \
            and (board.board[self.x][self.y - 4] != 'X') \
            and (board.board[self.x + 1][self.y - 1] != 'X') \
                and (board.board[self.x + 1][self.y - 4] != 'X'):
            if (board.board[self.x][self.y - 1] != 'X') \
                and (board.board[self.x][self.y - 4] != 'X') \
                and (board.board[self.x + 1][self.y - 1] != 'X') \
                    and (board.board[self.x + 1][self.y - 4] != 'X'):
                bomber.score += 20
            for i in range(len(list_enem)):
                if (self.x == list_enem[i].y) \
                        and (self.y - 4 == list_enem[i].x):
                    list_enem[i].life = 0
                    bomber.score += 100
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.x + i][self.y - 4 + j] = 'e'

        end = Timer(0.8, self.remove, [self.x, self.y, board])
        end.start()

        if (self.x == bomber.x and self.y == bomber.y):
            bomber.lives -= 1
            bomber.x = 2
            bomber.y =4
            bomber.position(board)
        if ((self.x + 2) == bomber.x and self.y == bomber.y):
            bomber.lives -= 1
            bomber.x = 2
            bomber.y =4
            bomber.position(board)
        if ((self.x - 2) == bomber.x and self.y == bomber.y):
            bomber.lives -= 1
            bomber.x = 2
            bomber.y =4
            bomber.position(board)
        if (self.x == bomber.x and (self.y + 4) == bomber.y):
            bomber.lives -= 1
            bomber.x = 2
            bomber.y =4
            bomber.position(board)
        if (self.x == bomber.x and (self.y - 4) == bomber.y):
            bomber.lives -= 1
            bomber.x = 2
            bomber.y =4
            bomber.position(board)

        
    def remove(self, x, y, board):
        for i in range(0, 2):
            for j in range(0, 4):
                if (board.board[x + 2][y] != 'X') \
                    and (board.board[x + 3][y] != 'X') \
                    and (board.board[x + 2][y + 3] != 'X') \
                        and (board.board[x + 3][y + 3] != 'X'):
                    board.board[self.x + 2 + i][self.y + j] = ' '

                if (board.board[x - 1][y] != 'X') \
                    and (board.board[x - 2][y] != 'X') \
                    and (board.board[x - 1][y + 3] != 'X') \
                        and (board.board[x - 2][y + 3] != 'X'):
                    board.board[self.x - 2 + i][self.y + j] = ' '

                if (board.board[x][y + 4] != 'X') \
                    and (board.board[x][y + 7] != 'X') \
                    and (board.board[x + 1][y + 4] != 'X') \
                        and (board.board[x + 1][y + 7] != 'X'):
                    board.board[self.x + i][self.y + 4 + j] = ' '

                if (board.board[x][y - 1] != 'X') \
                    and (board.board[x][y - 4] != 'X') \
                    and (board.board[x + 1][y - 1] != 'X') \
                        and (board.board[x + 1][y - 4] != 'X'):
                    board.board[self.x + i][self.y - 4 + j] = ' '

                board.board[self.x + i][self.y + j] = ' '

    def pos(self, x, y):
        if(self.live == 0):
            for i in range(0, 2):
                for j in range(0, 4):
                    self.bomb[x + i][y + j] = 'O'
            self.x = x
            self.y = y
            self.live = 1
