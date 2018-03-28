from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are disallowed as intended
class PawnDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhitePawnFromA2ToA4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(B2, A4))

    def testMoveWhitePawnFromF6ToF7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(A6, F7))

    def testMoveWhitePawnFromD2ToD3ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.pawn, self.testUtility.getMove(A2, D3)),
                                            D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackPawnFromA7ToA5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(G7, A5))

    def testMoveBlackPawnFromF7ToF6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(A7, F6))

    def testMoveBlackPawnFromD7ToD6ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.pawn, self.testUtility.getMove(A7, D6)),
                                            D5)
