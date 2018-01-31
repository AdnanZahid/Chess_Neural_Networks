from src.models.board import *
from src.models.pieces.strategies.move_strategy import *

class UnlimitedMoveStrategy(MoveStrategy):
    
    def generateMove(position,fileRankPair):
    
        possibleMovesToSquaresList = []
        newPosition = position + fileRankPair
        
        while Board.checkIfSquareIsNotNil(newPosition)\
            and Board.sharedInstance.checkIfEmptyOrEnemyPieceExists(color,newPosition)\
            and Board.sharedInstance.checkForClearPath(EvaluationMove(position,newPosition)):
                
                possibleMovesToSquaresList.append(newPosition)                
                newPosition = newPosition + fileRankPair
        
        return possibleMovesToSquaresList
        