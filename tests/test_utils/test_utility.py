import unittest
from PieceFactory import *
from Constants import *
from Structures import *

# /////////////////////////////////////////
# // Operator overloading for Unit Tests //
# /////////////////////////////////////////

class TestUtility(unittest.TestCase):

    def __init__(self,board):
        self.board = board

    # GET PIECE by PieceValue and perform the MOVE on it, returns TRUE
    def movePiece(self,pieceValue,move):
        
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue,move.fromSquare,None,self.board)
        
        # PUTTING the PIECE on the given SQUARE
        self.assertTrue(self.board.putPieceOnPosition(piece,piece.position,False))
        
        # MOVING the PIECE to the given SQUARE - EXPECTING it to PASS
        self.movePieceToSquare(piece,move.toSquare)

        piece.position = move.toSquare

        return piece

    # GET PIECE and move on it to the SQUARE, asserts TRUE
    def movePieceToSquare(self,piece,toSquare):
        self.assertTrue(self.board.movePiece(EvaluationMove(piece.position,toSquare),False))

    # GET PIECE by PieceValue and perform the MOVE on it, returns FALSE
    def failToMovePiece(self,pieceValue,move):
        
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue,move.fromSquare,None)

        # PUTTING the PIECE on the given SQUARE
        self.assertTrue(self.board.putPieceOnPosition(piece,piece.position,False))
        
        # MOVING the PIECE to the given SQUARE - EXPECTING it to FAIL
        invalidMove(piece,move.toSquare)
        
        return piece

    # GET PIECE and move on it to the SQUARE, asserts FALSE
    def invalidMove(self,piece,toSquare):
        self.assertFalse(self.board.movePiece(EvaluationMove(piece.position,toSquare),False))

    # GET two SQUARE's and make a MOVE out of them
    def getMove(self,fromSquare,toSquare):    
        return EvaluationMove(fromSquare,toSquare)

    # GET PIECE by PieceValue, place it on the SQUARE and then try getting a non-nil value
    def isPieceExists(self,pieceValue,square):
        
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue,square,None)
        
        # PUTTING the PIECE on the given SQUARE - self.assertS TRUE
        self.assertTrue(self.board.putPieceOnPosition(piece,square,False))
        
        # GET PIECE from the given SQUARE - self.assertS NON NIL
        self.assertIsNotNone(self.board.getPieceOnPosition(square))
        
        # COMPARE the given PIECE and PIECE returned from the SQUARE - self.assertS TRUE
        self.assertTrue(piece == self.board.getPieceOnPosition(square))

    # GET PIECE by PieceValue and then place it on the SQUARE
    def movePieceValueToSquare(self,pieceValue,square):
        
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue,square,None)
        
        # PUTTING the PIECE on the given SQUARE - self.assertS TRUE
        self.assertTrue(self.board.putPieceOnPosition(piece,square,False))
        
        return piece

    # GET POSSIBLE MOVES LIST from PIECE
    def generateAllMoves(self,piece):
        return (piece.moveStrategy.generateAllMoves(piece.position))

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
