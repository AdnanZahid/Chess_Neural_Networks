from src.others.utility import *


# This class handles all the piece-centric logic
class Piece:

    def __init__(self, position, color, strategy):
        self.position = position
        self.color = color
        self.strategy = strategy
        self.hasMoved = False
        self.captured = False
        self.directionsList = []
        self.id = (position.rank * 10) + position.file

    def updatePosition(self, toSquare):
        self.position = toSquare
        self.hasMoved = True

    def __eq__(self, other):
        # "other" variable may be EmptyPiece
        # In that case return False, since piece can never be equal to EmptyPiece
        if other == EmptyPiece or other == None:
            return False
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __ne__(self, other):
        return ~(self == other)

    def __repr__(self):
        return "{} at {}".format(self.symbol, self.position)

    def canMovePiece(self, board, toSquare, player=None):
        if player:
            player.lastMoveType = MoveType.normal

        move = EvaluationMove(self.position, toSquare)
        result = Utility.isMoveInCorrectDirection(move, self.directionsList, self.strategy) \
                 and board.checkIfSquareIsNotNil(toSquare) \
                 and board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare) \
                 and board.checkForClearPath(move)

        if result and player:
            player.lastMoveType = MoveType.normal
        return result


class EmptyPiece:
    def __init__(self):
        pass
