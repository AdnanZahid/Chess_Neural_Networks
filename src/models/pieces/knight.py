from src.models.pieces.piece import *
from src.models.pieces.strategies.limited_move_strategy import *
from src.others.utility import *


# This class handles all the knight logic
class Knight(Piece):

    def __init__(self, color, position, hasMoved, delegate, board):
        if color == Color.white:
            self.symbol = Symbols.white_knight
        else:
            self.symbol = Symbols.black_knight

        self.initialize(color, position, hasMoved, delegate, board)
        self.directionsList = []
        self.value = abs(Values.knight)

        # Knight directions
        self.directionsList.append((1, 2))
        self.directionsList.append((2, 1))

        self.directionsList.append((-1, 2))
        self.directionsList.append((-2, 1))

        self.directionsList.append((1, -2))
        self.directionsList.append((2, -1))

        self.directionsList.append((-1, -2))
        self.directionsList.append((-2, -1))

        self.moveStrategy = LimitedMoveStrategy(self, color, self.directionsList, board)

    def moveToSquare(self, toSquare):

        result = self.move(EvaluationMove(self.position, toSquare)) \
                 and self.board.checkIfSquareIsNotNil(toSquare) \
                 and self.board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare)

        # Check for check on a new board with previous configurations
        if self.delegate:
            result = result and self.delegate.isUnderCheckOnNewBoard(self, toSquare)

        return result

    def move(self, move):
        result = False

        for direction in self.directionsList:
            result = direction == getFileAndRankAdvance(EvaluationMove(self.position, move.toSquare))
            if result:
                break

        return result
