from tests.test_utils.test_utility import *


# This class tests if queen legal moves are disallowed as intended
class QueenDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(A3, H8))

    def testMoveWhiteQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(H3, A8))

    def testMoveWhiteQueenFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.queen, self.testUtility.getMove(H1, E5)),
                                            F4)

    def testMoveWhiteQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(B2, A8))

    def testMoveWhiteQueenFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(C3, A8))

    def testMoveWhiteQueenFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.queen, self.testUtility.getMove(A1, D5)),
                                            F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(A2, H8))

    def testMoveBlackQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(E5, A8))

    def testMoveBlackQueenFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(D8, E5)),
            F4)

    def testMoveBlackQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(F7, A8))

    def testMoveBlackQueenFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(D2, A8))

    def testMoveBlackQueenFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(A1, D5)),
            F5)
