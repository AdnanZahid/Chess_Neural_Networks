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

    def __repr__(self):
        return "{} at {}".format(self.symbol, self.position)

    def canMovePiece(self, board, toSquare, player=None):
        if player:
            player.lastMoveType = MoveType.normal

        move = EvaluationMove(self.position, toSquare)
        return Utility.isMoveInCorrectDirection(move, self.directionsList, self.strategy) \
               and board.checkIfSquareIsNotNil(toSquare) \
               and board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare) \
               and board.checkForClearPath(move)


class EmptyPiece:
    def __init__(self):
        pass
