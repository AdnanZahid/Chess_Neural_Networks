from tests.test_utils.test_utility import *


# This class tests if rook legal moves are blocked as intended
class RookCapturesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        # These 3 methods will wipe the slate clean so we can begin anew
        self.board.setupEmptyBoard()
        self.gameLogic.whitePlayer.clearPlayerData()
        self.gameLogic.blackPlayer.clearPlayerData()

    # ///////////
    # // WHITE //
    # ///////////

    def testCaptureWhiteRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.rook, A8)
        self.testUtility.move(Values.rook, self.testUtility.getMove(A1, A8))

    def testCaptureWhiteRookFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.rook, A1)
        self.testUtility.move(Values.rook, self.testUtility.getMove(H1, A1))

    def testCaptureWhiteRookFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.rook, E4)
        self.testUtility.moveValueToSquare(-Values.rook, F4)
        self.testUtility.validMove( \
            self.testUtility.move(Values.rook, \
                                  self.testUtility.getMove(D4, E4)), F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.rook, A8)
        self.testUtility.move(-Values.rook, self.testUtility.getMove(A1, A8))

    def testCaptureBlackRookFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.rook, A1)
        self.testUtility.move(-Values.rook, self.testUtility.getMove(H1, A1))

    def testCaptureBlackRookFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.rook, E4)
        self.testUtility.moveValueToSquare(Values.rook, F4)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.rook, \
                                  self.testUtility.getMove(D4, E4)), F4)
