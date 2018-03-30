from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are disallowed as intended
class PawnDisallowMovesTests(unittest.TestCase):

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

    def testFailToMoveWhitePawnFromB2ToA4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(B2, A4))

    def testFailToMoveWhitePawnFromA6ToF7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(A6, F7))

    def testFailToMoveWhitePawnFromA2ToD3ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(A2, D3)),
                                            D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testFailToMoveBlackPawnFromG7ToA5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(G7, A5))

    def testFailToMoveBlackPawnFromA7ToF6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(A7, F6))

    def testFailToMoveBlackPawnFromA7ToD6ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(A7, D6)),
                                            D5)
