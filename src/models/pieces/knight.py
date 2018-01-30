import Constants
import Structures
from Piece import *
from LimitedMoveStrategy import *
from Utility import *

# This class handles all the knight logic
class Knight(Piece):
    
    def __init__(self,color,position,hasMoved,delegate,board):
        self.initialize(color,position,hasMoved,delegate,board)
        self.directionsList = []       
        self.symbol = Symbols.knight
        self.value = abs(Values.knight)
        
        # Knight directions
        self.directionsList.append(( 1,  2))
        self.directionsList.append(( 2,  1))
        
        self.directionsList.append((-1,  2))
        self.directionsList.append((-2,  1))
        
        self.directionsList.append(( 1, -2))
        self.directionsList.append(( 2, -1))
        
        self.directionsList.append((-1, -2))
        self.directionsList.append((-2, -1))
        
        self.moveStrategy = LimitedMoveStrategy(color,self.directionsList)
    
    def moveToSquare(self,toSquare):
        return self.move(self.position,toSquare,self.directionsList)

    def move(self,position,toSquare,directionsList):
        
        result = False
        
        for direction in self.directionsList:
            result = direction == getFileAndRankAdvance(EvaluationMove(position,toSquare))
            if result:
                break
        
        return result
        