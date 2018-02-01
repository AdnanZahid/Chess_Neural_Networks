import os
from pygame import *
from src.models.pieces.piece import *

# Constants
square_size = 100
columns, rows = 8, 8
screen_size = (columns * square_size,rows * square_size)
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)

# This class handles all the view related activity
class View:

	def __init__(self,board):
		possibleMoves = []
		while not(self.isGameOver()):
			# Initialization
			init()
			screen = display.set_mode(screen_size)

			# Events
			for e in event.get():
				if e.type == QUIT:
					gameOver = True
				elif e.type == MOUSEBUTTONUP:
					position = mouse.get_pos()
					x,y = self.convertCoordinatesForModel(position[0],position[1])
					possibleMoves = self.getPossibleMoves(x,y,board)

			# Drawing
			screen.fill(white_color)
			self.draw(screen,board,possibleMoves)
			display.flip()

			# Clock ticking
			time.Clock().tick(60)

	def draw(self,screen,board,possibleMoves):
		self.drawSquares(screen)
		self.drawPieces(screen,board)
		self.drawPossibleMoves(screen,possibleMoves)

	def drawSquares(self,screen):
		for x in range(columns):
			for y in range(rows):
				if (x + y) % 2:
					draw.rect(screen,white_color,Rect(x*square_size,y*square_size,square_size,square_size))
				else:
					draw.rect(screen,black_color,Rect(x*square_size,y*square_size,square_size,square_size))

	def drawPieces(self,screen,board):
		for x in range(len(board.grid)):
			for y in range(len(board.grid[0])):
				piece = board.grid[x][y]
				if not(piece == NilPiece or piece == EmptyPiece):
					xPosition,yPosition = self.convertCoordinatesForGUI(x,y)
					path = os.path.dirname(__file__)+"/images/"+piece.symbol+".png"
					sprite = image.load(path)
					sprite = transform.scale(sprite, (square_size, square_size))
					screen.blit(sprite,Rect(xPosition,yPosition,square_size,square_size))

	def getPossibleMoves(self,x,y,board):
		piece = board.grid[x][y]
		return piece.moveStrategy.generateAllMoves(piece.position)

	def drawPossibleMoves(self,screen,squares):
		for square in squares:
			x,y = self.convertCoordinatesForGUI(square.rank,square.file)
			surface = Surface((square_size,square_size))
			surface.set_alpha(100)
			surface.fill(green_color)
			screen.blit(surface,(x,y))

	def convertCoordinatesForGUI(self,x,y):
		# Transform and offset according to our view
		# Transform = +7, because view is inverted
		# Offset = -2, because first 2 columns and rows are filled with NIL values
		# Multiplier = square_size, because each square needs to be a certain distance apart
		xPosition = (y - 2)*square_size
		yPosition = (7 - (x - 2))*square_size
		return xPosition,yPosition

	def convertCoordinatesForModel(self,x,y):
		# Transform and offset according to our view
		# Transform = +7, because view is inverted
		# Offset = +2, because first 2 columns and rows are filled with NIL values
		# Divider = square_size, because each square is a certain distance apart in GUI but adjacent in model
		xPosition = 7-(y/square_size)+2
		yPosition = ((x/square_size)+2)
		return xPosition,yPosition

	def isGameOver(self):
		return False
