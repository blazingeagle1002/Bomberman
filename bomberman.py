import os
import getch
import time
from random import randint

class Board:
	def __init__(self):
		self.height = 42
		self.width = 92
		self.board = [[' ' for x in range(self.width)] for y in range(self.height)]
		self.__bounds()

	def __bounds(self):
		for x in range(self.height):
			if x<2:
				for y in range(self.width):
					self.board[x][y]='X'
			elif x > (self.height-3):
				for y in range(self.width):
					self.board[x][y]='X'
			else:
				self.board[x][0]='X' 
				self.board[x][1]='X' 
				self.board[x][2]='X' 
				self.board[x][3]='X'
				self.board[x][self.width-1]='X' 
				self.board[x][self.width-2]='X' 
				self.board[x][self.width-3]='X' 
				self.board[x][self.width-4]='X'
	

	def border(self):
		for x in range(2,self.height-2):
			for y in range(4,self.width-4):
				if self.board[x][y] == 'B':
					self.board[x][y] = ' '

class walls:
	def __init__(self,board):
		self.__wall(board)

	def __wall(self,board):
		for y in range(2,board.height-2): 
			if (y%4==0) or (y%4==1):
				for x in range(4,board.width-4):
					if (x%8 ==0) or (x%8 ==1) or (x%8 ==2) or (x%8 ==3):
						board.board[y][x] = 'X'			

class person:
	def __init__(self):
		self.x =  0
		self.y = 0
		self.width = 4
		self.height = 2

class bomberman(person):
	def __init__(self):
		self.lives = 3
		self.x = 2
		self.y = 4

	def position(self,board):
		for i in range(0,2):
			for j in range(0,4):
				board.board[self.x+i][self.y+j]='B'

class Brick:
	def __init__(self,board):
		self.__align_bricks(board)
		self.cnt = 40
	def	__align_bricks(self,board):
		val = 0
		while(val!=40):
			x=randint(2,89)
			y=randint(4,37)
			if(board.board[y][x] == ' ') and (board.board[y+1][x] == ' ') and (board.board[y][x+3] == ' ') and (board.board[y+1][x+3] == ' '):
				if (x%4==0) and (y%2==0):
					val+=1
					for i in range(0,2):
						for j in range(0,4):
							board.board[y+i][x+j]='\\'


class Enemy(person):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.__position()

	def __position():
		x = randint(4,37)
		y = randint(4,89)


class Main(object):
	def __init__(self):
		pass
	def __printer(self,board):
		for x in range(board.height):
			print(''.join(board.board[x]))

	def init(self,board):
		board.border()
		Wall=walls(board)
		bomber=bomberman()
		bomber.position(board)
		brick=Brick(board)
		os.system('clear')
		
		while (1):
			self.__printer(board)
			board.border()
			Wall=walls(board)
			val=getch.getch()
			if val == 'q':
				break
			elif val == 'a':
				if board.board[bomber.x][bomber.y-4] == ' ' and board.board[bomber.x+1][bomber.y-4] == ' ' :
					bomber.y-=4
			elif val == 'd':
				if board.board[bomber.x][bomber.y+7] == ' ' and board.board[bomber.x+1][bomber.y+7] == ' ' :
					bomber.y+=4
			elif val == 'w':
				if board.board[bomber.x-2][bomber.y] == ' ' and board.board[bomber.x-2][bomber.y+3] == ' ':
					bomber.x-=2
			elif val == 's':
				if board.board[bomber.x+3][bomber.y] == ' ' and board.board[bomber.x+3][bomber.y+3] == ' ':
					bomber.x+=2
			bomber.position(board)

board=Board()
main=Main()
main.init(board)