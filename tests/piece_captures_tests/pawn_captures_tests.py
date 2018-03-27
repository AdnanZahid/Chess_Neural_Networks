from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are blocked as intended
class PawnCapturesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testCaptureWhitePawnFromA2ToB3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, B3)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(A2, B3))

    def testCaptureWhitePawnFromH6ToG7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, G7)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(H6, G7))

    def testCaptureWhitePawnFromD2ToE3ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, E3)
        self.testUtility.moveValueToSquare(-Values.pawn, D4)
        self.testUtility.validMove( \
            self.testUtility.move(Values.pawn, \
                                       self.testUtility.getMove(D2, E3)), D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackPawnFromA7ToB6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.pawn, B6)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(A7, B6))

    def testCaptureBlackPawnFromH5ToG4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.pawn, G4)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(H5, G4))

    def testCaptureBlackPawnFromE7ToD6ToE5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.pawn, D6)
        self.testUtility.moveValueToSquare(Values.pawn, E5)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.pawn, \
                                       self.testUtility.getMove(E7, D6)), E5)
