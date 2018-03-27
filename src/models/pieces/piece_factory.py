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

        # //////////////////
        # // WHITE PIECES //
        # //////////////////

        elif value == Values.king:
            piece = King(position, Color.white)
            piece.symbol = Symbols.white_king
        elif value == Values.queen:
            piece = Queen(position, Color.white)
            piece.symbol = Symbols.white_queen
        elif value == Values.rook:
            piece = Rook(position, Color.white)
            piece.symbol = Symbols.white_rook
        elif value == Values.knight:
            piece = Knight(position, Color.white)
            piece.symbol = Symbols.white_knight
        elif value == Values.bishop:
            piece = Bishop(position, Color.white)
            piece.symbol = Symbols.white_bishop
        elif value == Values.pawn:
            piece = Pawn(position, Color.white)
            piece.symbol = Symbols.white_pawn

        # //////////////////
        # // BLACK PIECES //
        # //////////////////

        elif value == -Values.king:
            piece = King(position, Color.black)
            piece.symbol = Symbols.black_king
        elif value == -Values.queen:
            piece = Queen(position, Color.black)
            piece.symbol = Symbols.black_queen
        elif value == -Values.rook:
            piece = Rook(position, Color.black)
            piece.symbol = Symbols.black_rook
        elif value == -Values.knight:
            piece = Knight(position, Color.black)
            piece.symbol = Symbols.black_knight
        elif value == -Values.bishop:
            piece = Bishop(position, Color.black)
            piece.symbol = Symbols.black_bishop
        elif value == -Values.pawn:
            piece = Pawn(position, Color.black)
            piece.symbol = Symbols.black_pawn

        return piece
