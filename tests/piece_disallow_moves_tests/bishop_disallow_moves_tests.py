from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are disallowed as intended
class BishopDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(A1, A8))

    def testMoveWhiteBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(H1, A1))

    def testMoveWhiteBishopFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(D4, D5)),
            F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(A1, A8))

    def testMoveBlackBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(H1, A1))

    def testMoveBlackBishopFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(D4, D5)),
            F4)
