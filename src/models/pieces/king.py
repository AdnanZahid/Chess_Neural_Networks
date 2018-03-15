from src.models.pieces.piece import *
from src.models.pieces.strategies.limited_move_strategy import *
from src.others.utility import *


# This class handles all the king logic
class King(Piece):

    def __init__(self, color, position, hasMoved, delegate, board):
        super().__init__(color, position, hasMoved, delegate, board)

        self.value = abs(Values.king)

        if color == Color.white:
            self.symbol = Symbols.white_king
        else:
            self.symbol = Symbols.black_king

        # King directions
        self.directionsList.append((1, 1))
        self.directionsList.append((1, -1))
        self.directionsList.append((-1, 1))
        self.directionsList.append((-1, -1))

        self.directionsList.append((1, 0))
        self.directionsList.append((0, 1))
        self.directionsList.append((-1, 0))
        self.directionsList.append((0, -1))

        self.moveStrategy = LimitedMoveStrategy(self, color, self.directionsList, board)

        # Set king property of player for later use (castling, check and checkmate)
        if delegate:
            delegate.setKing(self)

    def move(self, move):
        result = False

        for direction in self.directionsList:
            result = direction == getFileAndRankAdvance(EvaluationMove(self.position, move.toSquare))
            if result:
                break

        return result
