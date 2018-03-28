from tests.test_utils.test_utility import *


# This class tests if knight legal moves are blocked as intended
class KnightBlockMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testBlockWhiteKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.knight, C2)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(A1, C2))

    def testBlockWhiteKnightFromH1ToG3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.knight, G3)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(H1, G3))

    def testBlockWhiteKnightFromD6ToE6ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.knight, E4)
        self.testUtility.moveValueToSquare(Values.knight, F6)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(Values.knight, \
                                             self.testUtility.getMove(D6, E4)), F6)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlockBlackKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.knight, C2)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(A1, C2))

    def testBlockBlackKnightFromH1ToG3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.knight, G3)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(H1, G3))

    def testBlockBlackKnightFromD4ToE6ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.knight, E6)
        self.testUtility.moveValueToSquare(-Values.knight, F4)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(-Values.knight, \
                                             self.testUtility.getMove(D4, E6)), F4)
