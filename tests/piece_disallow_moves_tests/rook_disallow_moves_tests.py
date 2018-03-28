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

    def testMoveWhiteRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A1, H8))

    def testMoveWhiteRookFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(H8, C1))

    def testMoveWhiteRookFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A1, H8))

    def testMoveBlackRookFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(H8, C5))

    def testMoveBlackRookFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)
