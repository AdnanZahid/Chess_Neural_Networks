import unittest

from src.models.game_logic import *
from src.others.structures import *


# This class tests if game logic is working properly
class GameLogicTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    def testmove(self):
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
