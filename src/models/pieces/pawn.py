from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the pawn logic
class Pawn(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.value = Values.pawn

        # Pawn directions

        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, self.pawnMoveDirection(1)))
        self.directionsList.append((0, self.pawnMoveDirection(2)))

        self.directionsList.append((-1, self.pawnMoveDirection(1)))
        self.directionsList.append((1, self.pawnMoveDirection(1)))

    def pawnMoveDirection(self, number):
        return number * self.color
