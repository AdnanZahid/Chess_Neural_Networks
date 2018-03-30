from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are blocked as intended
class BishopCapturesTests(unittest.TestCase):

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

    def testCaptureWhiteBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, H8)
        self.testUtility.move(Values.bishop, self.testUtility.getMove(A1, H8))

    def testCaptureWhiteBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, A8)
        self.testUtility.move(Values.bishop, self.testUtility.getMove(H1, A8))

    def testCaptureWhiteBishopFromD4ToE5ToC3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, E5)
        self.testUtility.moveValueToSquare(-Values.bishop, C3)
        self.testUtility.validMove( \
            self.testUtility.move(Values.bishop, \
                                       self.testUtility.getMove(D4, E5)), C3)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.bishop, H8)
        self.testUtility.move(-Values.bishop, self.testUtility.getMove(A1, H8))

    def testCaptureBlackBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.bishop, A8)
        self.testUtility.move(-Values.bishop, self.testUtility.getMove(H1, A8))

    def testCaptureBlackBishopFromD4ToE5ToC3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.bishop, E5)
        self.testUtility.moveValueToSquare(Values.bishop, C3)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.bishop, \
                                       self.testUtility.getMove(D4, E5)), C3)
