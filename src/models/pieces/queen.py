from src.others.constants import *
from src.others.structures import *
from src.others.utility import *
from src.models.board import *
from src.models.pieces.piece import *
from src.models.pieces.strategies.unlimited_move_strategy import *

# This class handles all the queen logic
class Queen(Piece):
    
    def __init__(self,color,position,hasMoved,delegate,board):
        if color == Color.white:
            self.symbol = Symbols.white_queen
        else:
            self.symbol = Symbols.black_queen

        self.initialize(color,position,hasMoved,delegate,board)
        self.directionsList = []
        self.value = abs(Values.queen)
        
        # Queen directions

        # Bishop directions
        self.directionsList.append(( 1,  1))
        self.directionsList.append(( 1, -1))
        self.directionsList.append((-1,  1))
        self.directionsList.append((-1, -1))
        
        # Rook directions
        self.directionsList.append(( 1,  0))
        self.directionsList.append(( 0,  1))
        self.directionsList.append((-1,  0))
        self.directionsList.append(( 0, -1))
        
        self.moveStrategy = UnlimitedMoveStrategy(self,color,self.directionsList,board)
    
    def move(self,move):        
        result = False
        
        if fileOrRankAdvanceBothCheck(EvaluationMove(move.fromSquare,move.toSquare)):
            fileRankPair = getFileAndRankAdvance(EvaluationMove(move.fromSquare,move.toSquare))
            if abs(fileRankPair[0]) == abs(fileRankPair[1]):
                result = True

        elif fileOrRankAdvanceExclusiveCheck(EvaluationMove(move.fromSquare,move.toSquare)):            
            result = True
        
        return result
