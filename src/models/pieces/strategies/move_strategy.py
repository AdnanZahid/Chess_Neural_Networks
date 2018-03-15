# This class manages mobility and list of moves for a piece
class MoveStrategy:

    def __init__(self, piece, color, directionsList, board):
        self.piece = piece
        self.color = color
        self.directionsList = directionsList
        self.board = board

    def getMobility(self, position):
        return len(self.generateAllPossibleTargetSquares(position))

    def generateAllPossibleTargetSquares(self, checkCurrentTurn = True):

        possibleMovesToSquaresList = []

        if checkCurrentTurn == False:
            delegate = self.piece.delegate
            self.piece.delegate = None

        if self.color == self.board.currentTurnColor or checkCurrentTurn == False:
            for direction in self.directionsList:
                possibleMovesToSquaresList.extend(self.generatePossibleTargetSquare(self.piece.position, direction))

        if checkCurrentTurn == False:
            self.piece.delegate = delegate

        return set(possibleMovesToSquaresList)
