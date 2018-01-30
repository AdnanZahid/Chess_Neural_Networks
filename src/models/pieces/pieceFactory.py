from Constants import *
from Structures import *
from Piece import *
from King import *
from Queen import *
from Rook import *
from Knight import *
from Bishop import *
from Pawn import *

class PieceFactory:
    
    @staticmethod
    def getPiece(value,position,move,board):
        
        if value == NilPiece:
            return NilPiece
            
        # //////////////////
        # // WHITE PIECES //
        # //////////////////
            
        elif value == Values.king:
            return King(Color.white,position,False,move,board)
        elif value == Values.queen:
            return Queen(Color.white,position,False,move,board)
        elif value == Values.rook:
            return Rook(Color.white,position,False,move,board)
        elif value == Values.knight:
            return Knight(Color.white,position,False,move,board)
        elif value == Values.bishop:
            return Bishop(Color.white,position,False,move,board)
        elif value == Values.pawn:
            return Pawn(Color.white,position,False,move,board)
            
        # //////////////////
        # // BLACK PIECES //
        # //////////////////
            
        elif value == -Values.king:
            return King(Color.black,position,False,move,board)
        elif value == -Values.queen:
            return Queen(Color.black,position,False,move,board)
        elif value == -Values.rook:
            return Rook(Color.black,position,False,move,board)
        elif value == -Values.knight:
            return Knight(Color.black,position,False,move,board)
        elif value == -Values.bishop:
            return Bishop(Color.black,position,False,move,board)
        elif value == -Values.pawn:
            return Pawn(Color.black,position,False,move,board)
            