import unittest

from src.models.game_logic import *
from src.others.structures import *


# This class tests if game logic is working properly
class GameLogicTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    def testMove(self):
        # Move knight on B1 to C3
        piece = self.board.getPieceOnPosition(B1)
        toSquare = C3
        self.gameLogic.move(EvaluationMove(piece.position, toSquare))
        self.assertTrue(piece.position == toSquare)

    def testChangeTurn(self):
        # Check current PLAYER color, should be white
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current PLAYER color, should be black
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.blackPlayer)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current PLAYER color, should be white again
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)

    def testChangeBoardColor(self):
        # Check current TURN color, should be white
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current TURN color, should be black
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.blackPlayer)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current TURN color, should be white again
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)

    def testGetFEN(self):
        self.assertTrue(self.gameLogic.getFEN() == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def testSetFEN1(self):
        # Set FEN #1
        self.gameLogic.setFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        # Test board description against the corresponding string
        self.assertTrue(
            self.gameLogic.board.toString() == "♖♘♗♕♔♗♘♖\n♙♙♙♙♙♙♙♙\n········\n········\n········\n········\n♟♟♟♟♟♟♟♟\n♜♞♝♛♚♝♞♜\n")
        # Test that current player is white player
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)
        # Test the castling rights
        self.assertTrue(self.gameLogic.whitePlayer.hasKingSideCastlingRights())
        self.assertTrue(self.gameLogic.whitePlayer.hasQueenSideCastlingRights())
        self.assertTrue(self.gameLogic.blackPlayer.hasKingSideCastlingRights())
        self.assertTrue(self.gameLogic.blackPlayer.hasQueenSideCastlingRights())
        # Test enpassant pawn
        self.assertTrue(self.gameLogic.board.movedPawn == None)
        # Test half move clock
        self.assertTrue(self.gameLogic.halfMoveClock == 0)
        # Test full move number
        self.assertTrue(self.gameLogic.fullMoveNumber == 1)

    def testSetFEN2(self):
        # Set FEN #2
        self.gameLogic.setFEN("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQk e3 0 1")
        # Test board description against the corresponding string
        self.assertTrue(
            self.gameLogic.board.toString() == "♖♘♗♕♔♗♘♖\n♙♙♙♙·♙♙♙\n········\n····♙···\n········\n········\n♟♟♟♟♟♟♟♟\n♜♞♝♛♚♝♞♜\n")
        # Test that current player is black player
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.blackPlayer)
        # Test the castling rights
        self.assertTrue(self.gameLogic.whitePlayer.hasKingSideCastlingRights())
        self.assertTrue(self.gameLogic.whitePlayer.hasQueenSideCastlingRights())
        self.assertTrue(self.gameLogic.blackPlayer.hasKingSideCastlingRights())
        self.assertFalse(self.gameLogic.blackPlayer.hasQueenSideCastlingRights())
        # Test enpassant pawn
        self.assertTrue(self.gameLogic.board.movedPawn.position.file == FileIndex.kE)
        self.assertTrue(self.gameLogic.board.movedPawn.position.rank == RankIndex.k4)
        # Test half move clock
        self.assertTrue(self.gameLogic.halfMoveClock == 0)
        # Test full move number
        self.assertTrue(self.gameLogic.fullMoveNumber == 1)

    def testSetFEN3(self):
        # Set FEN #3
        self.gameLogic.setFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w kq c6 0 2")
        # Test board description against the corresponding string
        self.assertTrue(
            self.gameLogic.board.toString() == "♖♘♗♕♔♗♘♖\n♙♙♙♙·♙♙♙\n········\n····♙···\n··♟·····\n········\n♟♟·♟♟♟♟♟\n♜♞♝♛♚♝♞♜\n")
        # Test that current player is white player
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.whitePlayer)
        # Test the castling rights
        self.assertFalse(self.gameLogic.whitePlayer.hasKingSideCastlingRights())
        self.assertFalse(self.gameLogic.whitePlayer.hasQueenSideCastlingRights())
        self.assertTrue(self.gameLogic.blackPlayer.hasKingSideCastlingRights())
        self.assertTrue(self.gameLogic.blackPlayer.hasQueenSideCastlingRights())
        # Test enpassant pawn
        self.assertTrue(self.gameLogic.board.movedPawn.position.file == FileIndex.kC)
        self.assertTrue(self.gameLogic.board.movedPawn.position.rank == RankIndex.k5)
        # Test half move clock
        self.assertTrue(self.gameLogic.halfMoveClock == 0)
        # Test full move number
        self.assertTrue(self.gameLogic.fullMoveNumber == 2)

    def testSetFEN4(self):
        # Set FEN #4
        self.gameLogic.setFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b - - 1 2")
        # Test board description against the corresponding string
        self.assertTrue(
            self.gameLogic.board.toString() == "♖♘♗♕♔♗·♖\n♙♙♙♙·♙♙♙\n·····♘··\n····♙···\n··♟·····\n········\n♟♟·♟♟♟♟♟\n♜♞♝♛♚♝♞♜\n")
        # Test that current player is black player
        self.assertTrue(self.gameLogic.currentPlayer == self.gameLogic.blackPlayer)
        # Test the castling rights
        self.assertFalse(self.gameLogic.whitePlayer.hasKingSideCastlingRights())
        self.assertFalse(self.gameLogic.whitePlayer.hasQueenSideCastlingRights())
        self.assertFalse(self.gameLogic.blackPlayer.hasKingSideCastlingRights())
        self.assertFalse(self.gameLogic.blackPlayer.hasQueenSideCastlingRights())
        # Test enpassant pawn
        self.assertTrue(self.gameLogic.board.movedPawn == None)
        # Test half move clock
        self.assertTrue(self.gameLogic.halfMoveClock == 1)
        # Test full move number
        self.assertTrue(self.gameLogic.fullMoveNumber == 2)
