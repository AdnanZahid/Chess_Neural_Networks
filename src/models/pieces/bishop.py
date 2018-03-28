from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the bishop logic
class Bishop(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.bishop

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_bishop
        else:
            self.symbol = Symbols.black_bishop

        # Bishop directions
        self.directionsList.append((1, 1))
        self.directionsList.append((1, -1))
        self.directionsList.append((-1, 1))
        self.directionsList.append((-1, -1))
