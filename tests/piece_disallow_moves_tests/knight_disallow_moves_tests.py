from tests.test_utils.test_utility import *


# This class tests if knight legal moves are disallowed as intended
class KnightDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testFailToMoveWhiteKnightFromG1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(G1, C2))

    def testFailToMoveWhiteKnightFromB7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(B7, F5))

    def testFailToMoveWhiteKnightFromA4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(Values.knight, self.testUtility.getMove(A4, F5)),
            E3)

    # ///////////
    # // BLACK //
    # ///////////

    def testFailToMoveBlackKnightFromH1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(H1, C2))

    def testFailToMoveBlackKnightFromA7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(A7, F5))

    def testFailToMoveBlackKnightFromA4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(A4, F5)),
            E3)
