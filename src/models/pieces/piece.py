from src.models.squares import *
from src.others.constants import *


# This class handles all the piece-centric logic
class Piece:

    def __init__(self, color, position, hasMoved, delegate, board):
        self.color = color
        self.position = position
        self.hasMoved = hasMoved
        self.delegate = delegate
        self.board = board
        self.captured = False
        self.directionsList = []
        self.id = (position.rank * 10) + position.file

    def updatePosition(self, toSquare, changeHasMoved):
        self.position = toSquare

        if changeHasMoved:
            self.hasMoved = True

    def moveToSquare(self, toSquare):
        result = self.move(EvaluationMove(self.position, toSquare)) \
                 and self.board.checkIfSquareIsNotNil(toSquare) \
                 and self.board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare) \
                 and self.board.checkForClearPath(EvaluationMove(self.position, toSquare))

        # Check for check on a new board with previous configurations
        if self.delegate:
            result = result and not (self.delegate.isUnderCheckOnNewBoard(self, toSquare))

        return result

    def __repr__(self):
        return "{} at {}".format(self.symbol, self.position)


class EmptyPiece:
    def __init__(self):
        self.symbol = Symbols.empty
