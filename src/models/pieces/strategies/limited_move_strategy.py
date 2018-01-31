from src.models.board import *
from src.models.pieces.strategies.move_strategy import *

class LimitedMoveStrategy(MoveStrategy):
    
    def generateMove(position,fileRankPair):
        
        possibleMovesToSquaresList = []
        newPosition = position + fileRankPair
        
        if Board.checkIfSquareIsNotNil(newPosition)\
            and Board.checkIfEmptyOrEnemyPieceExists(color,newPosition):
            
            possibleMovesToSquaresList.append(newPosition)
        
        return possibleMovesToSquaresList
