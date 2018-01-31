from src.models.pieces.piece_factory import *

# This class represents all the player information (while and black)
class Player:
    
    def __init__(self,color,board):
        self.color = color
        self.board = board
        self.piecesList = self.board.setupPieceBoard(color,self)
    
    def movePiece(move,checkCurrentTurn):
        result = False
        
        if self.board.movePiece(move,checkCurrentTurn):
            result = True
        
        return result
