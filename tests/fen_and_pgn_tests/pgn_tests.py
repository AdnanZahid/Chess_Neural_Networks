import unittest

from src.models.game_logic import *


# This class tests if PGN logic is working properly
class PGNTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    def testSetPGN1(self):
        # Set PGN #1
        self.gameLogic.pgn_helper.setPGN("sample1.pgn")

    def testSetPGN2(self):
        # Set PGN #2
        self.gameLogic.pgn_helper.setPGN("sample2.pgn")
