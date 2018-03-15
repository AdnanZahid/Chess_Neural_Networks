from src.models.pieces.piece import *
from src.models.pieces.strategies.unlimited_move_strategy import *
from src.others.utility import *


# This class handles all the rook logic
class Rook(Piece):

    def __init__(self, color, position, hasMoved, delegate, board):
        super().__init__(color, position, hasMoved, delegate, board)

        self.value = abs(Values.rook)

        if color == Color.white:
            self.symbol = Symbols.white_rook
        else:
            self.symbol = Symbols.black_rook

        # Rook directions
        self.directionsList.append((1, 0))
        self.directionsList.append((0, 1))
        self.directionsList.append((-1, 0))
        self.directionsList.append((0, -1))

        self.moveStrategy = UnlimitedMoveStrategy(self, color, self.directionsList, board)

        # Set king(H file)/queen(A file) side rook property of player for later use (castling)
        if delegate:
            if self.position.file == FileIndex.kH:
                delegate.setKingSideRook(self)
            else:
                delegate.setQueenSideRook(self)

    def move(self, move):
        result = False

        if fileOrRankAdvanceExclusiveCheck(EvaluationMove(move.fromSquare, move.toSquare)):
            result = True

        return result
