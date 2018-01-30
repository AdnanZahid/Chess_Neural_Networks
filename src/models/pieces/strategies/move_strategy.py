# This class manages mobility and list of moves for a piece
class MoveStrategy:
    
    def __init__(self,color,directionsList):        
        self.color = color
        self.directionsList = directionsList
    
    def getMobility(position):        
        return len(generateAllMoves(position))
    
    def generateAllMoves(position):
        
        possibleMovesToSquaresList = []
        
        for direction in directionsList:
            possibleMovesToSquaresList.append(generateMove(position,direction))
        
        return possibleMovesToSquaresList
        