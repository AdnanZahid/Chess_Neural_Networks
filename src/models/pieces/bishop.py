from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the bishop logic
class Bishop(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.value = Values.bishop

        # Bishop directions
        self.directionsList.append((1, 1))
        self.directionsList.append((1, -1))
        self.directionsList.append((-1, 1))
        self.directionsList.append((-1, -1))
