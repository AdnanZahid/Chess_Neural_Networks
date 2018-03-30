from tests.test_utils.test_utility import *


# This class tests if king legal moves are blocked as intended
class KingBlockMovesTests(unittest.TestCase):

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

    def testBlockWhiteKingFromG7ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, H8)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(G7, H8))

    def testBlockWhiteKingFromD4ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(D4, D5))

    def testBlockWhiteKingFromD6ToE5ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(Values.king, \
                                             self.testUtility.getMove(D6, E5)), D5)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlockBlackKingFromC4ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, D4)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(C4, D4))

    def testBlockBlackKingFromA3ToA2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A2)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(A3, A2))

    def testBlockBlackKingFromD4ToE5ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(-Values.king, \
                                             self.testUtility.getMove(D4, E5)), D5)
