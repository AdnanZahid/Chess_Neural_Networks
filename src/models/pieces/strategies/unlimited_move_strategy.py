import Board
from MoveStrategy import *

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
        