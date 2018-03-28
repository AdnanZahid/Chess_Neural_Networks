from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the rook logic
class Rook(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.rook

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_rook
        else:
            self.symbol = Symbols.black_rook

        # Rook directions
        self.directionsList.append((1, 0))
        self.directionsList.append((0, 1))
        self.directionsList.append((-1, 0))
        self.directionsList.append((0, -1))
