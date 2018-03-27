from tests.test_utils.test_utility import *


# This class tests if queen legal moves are blocked as intended
class QueenCapturesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testCaptureWhiteQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, H8)
        self.testUtility.move(Values.queen, self.testUtility.getMove(A1, H8))

    def testCaptureWhiteQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A8)
        self.testUtility.move(Values.queen, self.testUtility.getMove(H1, A8))

    def testCaptureWhiteQueenFromD4ToE5ToF6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, F6)
        self.testUtility.validMove( \
            self.testUtility.move(Values.queen, \
                                       self.testUtility.getMove(D4, E5)), F6)

    def testCaptureWhiteQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A8)
        self.testUtility.move(Values.queen, self.testUtility.getMove(A1, A8))

    def testCaptureWhiteQueenFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A1)
        self.testUtility.move(Values.queen, self.testUtility.getMove(H1, A1))

    def testCaptureWhiteQueenFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E4)
        self.testUtility.moveValueToSquare(-Values.queen, F4)
        self.testUtility.validMove( \
            self.testUtility.move(Values.queen, \
                                       self.testUtility.getMove(D4, E4)), F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, H8)
        self.testUtility.move(-Values.queen, self.testUtility.getMove(A1, H8))

    def testCaptureBlackQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, A8)
        self.testUtility.move(-Values.queen, self.testUtility.getMove(H1, A8))

    def testCaptureBlackQueenFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, F4)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.queen, \
                                       self.testUtility.getMove(D4, E5)), F4)

    def testCaptureBlackQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, A8)
        self.testUtility.move(-Values.queen, self.testUtility.getMove(A1, A8))

    def testCaptureBlackQueenFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, A1)
        self.testUtility.move(-Values.queen, self.testUtility.getMove(H1, A1))

    def testCaptureBlackQueenFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, E4)
        self.testUtility.moveValueToSquare(Values.queen, F4)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.queen, \
                                       self.testUtility.getMove(D4, E4)), F4)
