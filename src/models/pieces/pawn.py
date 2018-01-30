import Constants
import Structures
import Board
from Piece import *
from LimitedMoveStrategy import *
from Utility import *

# This class handles all the pawn logic
class Pawn(Piece):
    
    def __init__(self,color,position,hasMoved,delegate,board):
        self.initialize(color,position,hasMoved,delegate,board)
        self.directionsList = []     
        self.symbol = Symbols.pawn
        self.value = abs(Values.pawn)
        
        # Pawn directions
        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, self.pawnMoveDirection(1)))
        self.directionsList.append((0, self.pawnMoveDirection(2)))
        
        self.directionsList.append((-1, self.pawnMoveDirection(1)))
        self.directionsList.append(( 1, self.pawnMoveDirection(1)))
        
        self.moveStrategy = LimitedMoveStrategy(color,self.directionsList)
    
    def moveToSquare(self,toSquare):
        result = False
        
        if self.board.checkIfSquareIsEmpty(toSquare):
            if   getFileAndRankAdvance(EvaluationMove(self.position,toSquare)) == self.directionsList[0]:               
                result = True
            elif getFileAndRankAdvance(EvaluationMove(self.position,toSquare)) == self.directionsList[1]\
            and self.hasMoved == False:
                result = self.board.checkForClearPath(EvaluationMove(self.position,toSquare))
        
        elif not(self.board.getPieceOnPosition(toSquare).color == color):

            fileAndRankAdvance = getFileAndRankAdvance(EvaluationMove(position,toSquare))
            result = fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]
        
        return result
    
    def pawnMoveDirection(self,number):        
        return number * self.color
