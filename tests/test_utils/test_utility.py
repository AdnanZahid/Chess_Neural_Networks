import unittest

from src.models.game_logic import *


# /////////////////////////////////////////
# // Operator overloading for Unit Tests //
# /////////////////////////////////////////

class TestUtility(unittest.TestCase):

    def __init__(self, board, player):
        self.board = board
        self.player = player

    # GET PIECE by PieceValue and perform the MOVE on it, returns TRUE
    def move(self, pieceValue, move):
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue, move.fromSquare)

        # PUTTING the PIECE on the given SQUARE
        self.assertTrue(self.board.putPieceOnPosition(piece, piece.position))

        # MOVING the PIECE to the given SQUARE - EXPECTING it to PASS
        self.moveToSquare(piece, move.toSquare)

        return piece

    # GET PIECE and move it to the SQUARE, asserts TRUE
    def moveToSquare(self, piece, toSquare):
        self.assertTrue(MoveGenerator.canMovePiece(piece, self.board, self.player, toSquare))
        self.assertTrue(self.board.movePiece(piece, toSquare))
        piece.updatePosition(toSquare)

    # GET PIECE and FAIL to move it to the SQUARE, asserts FALSE
    def failToMoveToSquare(self, piece, toSquare):
        self.assertFalse(MoveGenerator.canMovePiece(piece, self.board, self.player, toSquare))

    # GET PIECE by PieceValue and perform the MOVE on it, returns FALSE
    def failToMove(self, pieceValue, move):
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue, move.fromSquare)

        # PUTTING the PIECE on the given SQUARE
        self.assertTrue(self.board.putPieceOnPosition(piece, piece.position))

        # MOVING the PIECE to the given SQUARE - EXPECTING it to FAIL
        self.invalidMove(piece, move.toSquare)

        return piece

    # GET PIECE and move on it to the SQUARE on a completely NEW BOARD, asserts TRUE
    def validMove(self, piece, toSquare):
        self.board.putPieceOnPosition(piece, piece.position)
        self.assertTrue(self.board.movePiece(piece, toSquare))

    # GET PIECE and move on it to the SQUARE on a completely NEW BOARD, asserts TRUE
    def validMoveOnNewBoard(self, board, piece, toSquare):
        piece.board = board
        board.putPieceOnPosition(piece, piece.position)
        self.assertTrue(board.movePiece(piece, toSquare))

    # GET PIECE and move on it to the SQUARE, asserts FALSE
    def invalidMove(self, piece, toSquare):
        self.assertFalse(MoveGenerator.canMovePiece(piece, self.board, self.player, toSquare))

        # MOVING the PIECE to the given SQUARE on a completely NEW BOARD - EXPECTING it to PASS
        self.validMoveOnNewBoard(Board(), piece, toSquare)

    # GET two SQUARE's and make a MOVE out of them
    def getMove(self, fromSquare, toSquare):
        return EvaluationMove(fromSquare, toSquare)

    # GET PIECE by PieceValue, place it on the SQUARE and then try getting a non-nil value
    def isPieceExists(self, pieceValue, square):
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue, square)

        # PUTTING the PIECE on the given SQUARE - self.assertS TRUE
        self.assertTrue(self.board.putPieceOnPosition(piece, square))

        # GET PIECE from the given SQUARE - self.assertS NON NIL
        self.assertIsNotNone(self.board.getPieceOnPosition(square))

        # COMPARE the given PIECE and PIECE returned from the SQUARE - self.assertS TRUE
        self.assertTrue(piece == self.board.getPieceOnPosition(square))

    # GET PIECE by PieceValue and then place it on the SQUARE
    def moveValueToSquare(self, pieceValue, square):
        # GETTING a PIECE from the PIECE FACTORY - Given the PIECE VALUE and STARTING SQUARE
        piece = PieceFactory.getPiece(pieceValue, square)

        # PUTTING the PIECE on the given SQUARE - self.assertS TRUE
        self.assertTrue(self.board.putPieceOnPosition(piece, square))

        return piece

    # GET POSSIBLE MOVES LIST from PIECE
    def generateAllPossibleTargetSquares(self, piece):
        return MoveGenerator.generatePossibleTargetSquares(piece, self.board, self.player, isCheckForCheck=False)

    def checkEqualMoves(self, movesList1, movesList2):
        self.assertTrue(len(movesList1) == len(movesList2))
        self.assertTrue(sorted(movesList1) == sorted(movesList2))
