from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the knight logic
class Knight(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.knight

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_knight
            self.fenSymbol = FENSymbols.white_knight
        else:
            self.symbol = Symbols.black_knight
            self.fenSymbol = FENSymbols.black_knight

        # Knight directions
        self.directionsList.append((1, 2))
        self.directionsList.append((2, 1))

        self.directionsList.append((-1, 2))
        self.directionsList.append((-2, 1))

        self.directionsList.append((1, -2))
        self.directionsList.append((2, -1))

        self.directionsList.append((-1, -2))
        self.directionsList.append((-2, -1))

    # Separate method for knight since knight doesn't need "board.checkForClearPath(move)"
    # Which is used in Piece (parent class)
    def canMovePiece(self, board, toSquare, player=None, isCheckForCastling=True):

        move = Move(self.position, toSquare)
        result = Utility.isMoveInCorrectDirection(move, self.directionsList, self.strategy) \
                 and board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare)

        if result:
            player.lastMoveType = MoveType.normal
        return result
