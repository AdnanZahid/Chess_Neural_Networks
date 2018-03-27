from tests.test_utils.test_utility import *


# This class tests if king legal moves are blocked as intended
class KingCapturesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testCaptureWhiteKingFromG7ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, H8)
        self.testUtility.move(Values.king, self.testUtility.getMove(G7, H8))

    def testCaptureWhiteKingFromD4ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.move(Values.king, self.testUtility.getMove(D4, D5))

    def testCaptureWhiteKingFromD6ToE5ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.validMove( \
            self.testUtility.move(Values.king, \
                                       self.testUtility.getMove(D6, E5)), D5)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackKingFromC4ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, D4)
        self.testUtility.move(-Values.king, self.testUtility.getMove(C4, D4))

    def testCaptureBlackKingFromA3ToA2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, A2)
        self.testUtility.move(-Values.king, self.testUtility.getMove(A3, A2))

    def testCaptureBlackKingFromD4ToE5ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.king, \
                                       self.testUtility.getMove(D4, E5)), D5)
