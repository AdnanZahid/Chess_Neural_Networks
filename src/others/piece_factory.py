from src.models.pieces.bishop import *
from src.models.pieces.king import *
from src.models.pieces.knight import *
from src.models.pieces.pawn import *
from src.models.pieces.queen import *
from src.models.pieces.rook import *
from src.others.constants import *


class PieceFactory:

    @staticmethod
    def getPiece(value, position):

        if value == None:
            piece = None

        # Color assignment
        if value > 0:
            color = Color.white
        else:
            color = Color.black

        value = abs(value)

        if value == Values.king:
            piece = King(position, color, Strategy.jumping)
        elif value == Values.queen:
            piece = Queen(position, color, Strategy.sliding)
        elif value == Values.rook:
            piece = Rook(position, color, Strategy.sliding)
        elif value == Values.knight:
            piece = Knight(position, color, Strategy.jumping)
        elif value == Values.bishop:
            piece = Bishop(position, color, Strategy.sliding)
        elif value == Values.pawn:
            piece = Pawn(position, color, Strategy.jumping)

        return piece
