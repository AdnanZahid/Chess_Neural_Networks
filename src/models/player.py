from src.models.pieces.piece_factory import *

# This class represents all the player information (while and black)
class Player:
    
    def __init__(self,color,board):
        self.color = color
        self.board = board
        self.piecesList = self.board.setupPieceBoard(color,self)
    
    def movePiece(self,move,checkCurrentTurn):
        result = False
        
        if self.board.movePiece(move,checkCurrentTurn):
            result = True
        
        return result

    def setKing(self,king):
    	self.king = king

    def setKingSideRook(self,rook):
    	self.kingSideRook = rook

    def setQueenSideRook(self,rook):
    	self.queenSideRook = rook

    def getAllMoves(self):
    	movesList = []
    	for piece in self.piecesList:
    		movesList.extend(piece.moveStrategy.generateAllMoves())
    	return movesList

    def isUnderCheck(self):
    	for move in self.opponent.getAllMoves():
    		if move == self.king.position:
    			return True
    	return False

    def isUnderCheckMate(self):
        return False
