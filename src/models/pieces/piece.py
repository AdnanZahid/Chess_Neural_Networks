from src.others.constants import *
from src.others.utility import *


# This class handles all the piece-centric logic
class Piece:

    def __init__(self, position, color, strategy):
        self.position = position
        self.color = color
        self.strategy = strategy
        self.hasMoved = False
        self.directionsList = []
        self.id = (position.rank * 10) + position.file

    def updatePosition(self, toSquare):
        self.position = toSquare
        self.hasMoved = True

        if self.value == Values.pawn:
            from src.others.piece_factory import PieceFactory
            queen = None
            if self.color == Color.white and self.position.rank == RankIndex.k8:
                queen = PieceFactory.getPiece(Values.queen, self.position)
            elif self.color == Color.black and self.position.rank == RankIndex.k1:
                queen = PieceFactory.getPiece(-Values.queen, self.position)

            if queen:
                self.__dict__ = queen.__dict__
                self.__class__ = queen.__class__

    def __eq__(self, other):
        # "other" variable may be EmptyPiece
        # In that case return False, since piece can never be equal to EmptyPiece
        if other == None or other == EmptyPiece:
            return False
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __repr__(self):
        return "{} at {}".format(self.symbol, self.position)

    def canMovePiece(self, board, toSquare, player=None, isCheckForCastling=True):
        move = EvaluationMove(self.position, toSquare)
        result = Utility.isMoveInCorrectDirection(move, self.directionsList, self.strategy) \
                 and board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare) \
                 and board.checkForClearPath(move)

        if result and player:
            player.lastMoveType = MoveType.normal
        return result
