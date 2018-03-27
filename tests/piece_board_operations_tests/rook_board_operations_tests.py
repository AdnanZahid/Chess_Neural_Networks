from tests.test_utils.test_utility import *


# This class tests if rook legal moves are blocked as intended
class RookBoardOperationsTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testGetWhiteRookOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.isPieceExists(Values.rook, D4)

    def testPutWhiteRookOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.rook, D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testGetBlackRookOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.isPieceExists(-Values.rook, D4)

    def testPutBlackRookOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.rook, D4)
