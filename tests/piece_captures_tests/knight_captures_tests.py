from tests.test_utils.test_utility import *


# This class tests if knight legal moves are blocked as intended
class KnightCapturesTests(unittest.TestCase):

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

    def testCaptureWhiteKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.knight, C2)
        self.testUtility.move(Values.knight, self.testUtility.getMove(A1, C2))

    def testCaptureWhiteKnightFromH1ToG3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.knight, G3)
        self.testUtility.move(Values.knight, self.testUtility.getMove(H1, G3))

    def testCaptureWhiteKnightFromD6ToE6ToF2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.knight, E4)
        self.testUtility.moveValueToSquare(-Values.knight, F2)
        self.testUtility.validMove( \
            self.testUtility.move(Values.knight, \
                                       self.testUtility.getMove(D6, E4)), F2)

    # ///////////
    # // BLACK //
    # ///////////

    def testCaptureBlackKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.knight, C2)
        self.testUtility.move(-Values.knight, self.testUtility.getMove(A1, C2))

    def testCaptureBlackKnightFromH1ToG3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.knight, G3)
        self.testUtility.move(-Values.knight, self.testUtility.getMove(H1, G3))

    def testCaptureBlackKnightFromD4ToE6ToF8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.knight, E6)
        self.testUtility.moveValueToSquare(Values.knight, F8)
        self.testUtility.validMove( \
            self.testUtility.move(-Values.knight, \
                                       self.testUtility.getMove(D4, E6)), F8)
