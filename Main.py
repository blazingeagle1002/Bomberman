import tty
import termios
import sys
import os
from threading import Timer
from Board import Board
from Wall import Walls
from Brick import Brick
from Bomber import bomberman
from Bomb import Bomb
from Enemy import Enemy
from select import select


class Main:

    def __init__(self):
        board = Board()
        self.done_val=4
        self.time = 0
        self.init(board)

    def __printer(self, board, bomber):
        os.system('clear')
        for x in range(board.height):
            print(''.join(board.board[x]))
        print("LIVES:",bomber.lives,"   ","SCORE:",bomber.score,"   ","TIME:",200 - self.time)

    def __check(self, board, bomb, bomber):
        for x in range(42):
            for y in range(92):
                if (bomb.bomb[x][y] == 'O') and (board.board[x][y] == ' '):
                    board.board[x][y] = bomb.bomb[x][y]
        self.__printer(board, bomber)

    def __getchar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select([sys.stdin.fileno()], [], [], 0.8)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def init(self, board):
        board.border()
        Wall = Walls(board)
        bomber = bomberman()
        bomber.position(board)
        brick = Brick(board)
        bomb = Bomb()
        os.system('clear')
        list_enem = []
        for i in range(0, 4):
            x = Enemy(board)
            x.pos(board)
            list_enem.append(x)
        while (1):
            self.time += 1
            self.__check(board, bomb, bomber)
            board.border()
            Wall = Walls(board)
            val = self.__getchar()
            if val == 'q':
                print("\n")
                print("GAME OVER")
                break
            elif val == 'b':
                bomb.pos(bomber.x, bomber.y)
                t = Timer(3, bomb.explode, [bomb.x, bomb.y, board, bomber, list_enem])
                t.start()
            elif val is not None:
                bomber.move(board, val)
            bomber.position(board)
            done = []
            if bomber.lives == 0:
                print("\n GAME OVER \n")
            for i in range(self.done_val):
                done.append(0)
            for i in range(len(list_enem)):
                if(bomber.x == list_enem[i].y) \
                and (bomber.y == list_enem[i].x):
                    quit()
                done[i] = list_enem[i].move(board)
                list_enem[i].pos(board)
            for i in range(self.done_val):
                if(list_enem[i].life == 0):
                    del list_enem[i]
                    self.done_val -= 1
                    break
            if(self.done_val == 0):
                print("\n")
                print("SUCCESS")
                print("GAME COMPLETED")
                print("\n")
                break
            for i in range(len(list_enem)):
                if(done[i] == 1):
                    done[i] = 0
                    bomber.lives -= 1
                    bomber.x = 2
                    bomber.y = 4
                    bomber.position(board)
                    self.__check(board, bomb, bomber)
