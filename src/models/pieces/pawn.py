from src.others.constants import *
from src.others.structures import *
from src.others.utility import *
from src.models.board import *
from src.models.pieces.piece import *
from src.models.pieces.strategies.limited_move_strategy import *

# This class handles all the pawn logic
class Pawn(Piece):
    
    def __init__(self,color,position,hasMoved,delegate,board):
        if color == Color.white:
            self.symbol = Symbols.white_pawn
        else:
            self.symbol = Symbols.black_pawn

        self.initialize(color,position,hasMoved,delegate,board)
        self.directionsList = []
        self.value = abs(Values.pawn)
        
        # Pawn directions
        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, self.pawnMoveDirection(1)))
        self.directionsList.append((0, self.pawnMoveDirection(2)))
        
        self.directionsList.append((-1, self.pawnMoveDirection(1)))
        self.directionsList.append(( 1, self.pawnMoveDirection(1)))
        
        self.moveStrategy = LimitedMoveStrategy(self,color,self.directionsList,board)

    def move(self,move):
        result = False
        
        targetPiece = self.board.getPieceOnPosition(move.toSquare)

        if self.board.checkIfSquareIsEmpty(move.toSquare):
            if   getFileAndRankAdvance(EvaluationMove(self.position,move.toSquare)) == self.directionsList[0]:               
                result = True
            elif getFileAndRankAdvance(EvaluationMove(self.position,move.toSquare)) == self.directionsList[1]\
            and self.hasMoved == False:
                result = self.board.checkForClearPath(EvaluationMove(self.position,move.toSquare))
        
        elif not(targetPiece == NilPiece) and not(targetPiece.color == self.color):

            fileAndRankAdvance = getFileAndRankAdvance(EvaluationMove(self.position,move.toSquare))
            result = fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]
        
        return result
    
    def pawnMoveDirection(self,number):        
        return number * self.color
