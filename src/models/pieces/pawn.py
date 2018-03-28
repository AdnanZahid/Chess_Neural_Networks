from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the pawn logic
class Pawn(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.pawn

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_pawn
        else:
            self.symbol = Symbols.black_pawn

        # Pawn directions

        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, Pawn.pawnMoveDirection(self.color, 1)))
        self.directionsList.append((0, Pawn.pawnMoveDirection(self.color, 2)))

        self.directionsList.append((-1, Pawn.pawnMoveDirection(self.color, 1)))
        self.directionsList.append((1, Pawn.pawnMoveDirection(self.color, 1)))

    @staticmethod
    def pawnMoveDirection(color, number):
        return color * number
