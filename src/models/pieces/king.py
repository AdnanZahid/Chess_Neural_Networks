from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the king logic
class King(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.king

        # Symbol
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
