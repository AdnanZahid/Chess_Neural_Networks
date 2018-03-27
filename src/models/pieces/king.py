from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the king logic
class King(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.value = Values.king

        # King directions
        self.directionsList.append((1, 1))
        self.directionsList.append((1, -1))
        self.directionsList.append((-1, 1))
        self.directionsList.append((-1, -1))

        self.directionsList.append((1, 0))
        self.directionsList.append((0, 1))
        self.directionsList.append((-1, 0))
        self.directionsList.append((0, -1))
