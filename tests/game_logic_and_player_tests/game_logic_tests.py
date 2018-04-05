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

    def testSetFEN(self):
        self.gameLogic.setFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.gameLogic.setFEN("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
        self.gameLogic.setFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2")
        self.gameLogic.setFEN("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
