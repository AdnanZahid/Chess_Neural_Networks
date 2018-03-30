from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are blocked as intended
class PawnBlockMovesTests(unittest.TestCase):

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

    def testBlockWhitePawnFromA2ToA4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.pawn, A4)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(A2, A4))

    def testBlockWhitePawnFromH6ToH7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.pawn, H7)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(H6, H7))

    def testBlockWhitePawnFromD2ToD3ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.pawn, D3)
        self.testUtility.moveValueToSquare(Values.pawn, D4)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(Values.pawn, \
                                             self.testUtility.getMove(D2, D3)), D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlockBlackPawnFromA7ToA5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, A5)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(A7, A5))

    def testBlockBlackPawnFromH5ToH4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, H4)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(H5, H4))

    def testBlockBlackPawnFromE7ToE6ToE5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, E6)
        self.testUtility.moveValueToSquare(-Values.pawn, E5)
        self.testUtility.invalidMove( \
            self.testUtility.failToMove(-Values.pawn, \
                                             self.testUtility.getMove(E7, E6)), E5)
