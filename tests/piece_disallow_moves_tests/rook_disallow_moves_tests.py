from tests.test_utils.test_utility import *


# This class tests if rook legal moves are disallowed as intended
class RookDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testFailToMoveWhiteRookFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A1, H8))

    def testFailToMoveWhiteRookFromH8ToC1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(H8, C1))

    def testFailToMoveWhiteRookFromA4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testFailToMoveBlackRookFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A1, H8))

    def testFailToMoveBlackRookFromH8ToC5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(H8, C5))

    def testFailToMoveBlackRookFromA4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)
