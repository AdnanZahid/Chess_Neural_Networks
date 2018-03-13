from src.models.pieces.bishop import *
from src.models.pieces.king import *
from src.models.pieces.knight import *
from src.models.pieces.pawn import *
from src.models.pieces.queen import *
from src.models.pieces.rook import *


class PieceFactory:

    @staticmethod
    def getPiece(value, position, delegate, board):

        if value == None:
            return None

        # //////////////////
        # // WHITE PIECES //
        # //////////////////

        elif value == Values.king:
            return King(Color.white, position, False, delegate, board)
        elif value == Values.queen:
            return Queen(Color.white, position, False, delegate, board)
        elif value == Values.rook:
            return Rook(Color.white, position, False, delegate, board)
        elif value == Values.knight:
            return Knight(Color.white, position, False, delegate, board)
        elif value == Values.bishop:
            return Bishop(Color.white, position, False, delegate, board)
        elif value == Values.pawn:
            return Pawn(Color.white, position, False, delegate, board)

        # //////////////////
        # // BLACK PIECES //
        # //////////////////

        elif value == -Values.king:
            return King(Color.black, position, False, delegate, board)
        elif value == -Values.queen:
            return Queen(Color.black, position, False, delegate, board)
        elif value == -Values.rook:
            return Rook(Color.black, position, False, delegate, board)
        elif value == -Values.knight:
            return Knight(Color.black, position, False, delegate, board)
        elif value == -Values.bishop:
            return Bishop(Color.black, position, False, delegate, board)
        elif value == -Values.pawn:
            return Pawn(Color.black, position, False, delegate, board)
