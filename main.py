from src.models.board import *
from src.views.view import *

board = Board()
board.setupPieceBoard(Color.white,None)
board.setupPieceBoard(Color.black,None)
board.printBoard()

View(board)
