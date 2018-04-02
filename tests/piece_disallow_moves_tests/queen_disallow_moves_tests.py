from tests.test_utils.test_utility import *


# This class tests if queen legal moves are disallowed as intended
class QueenDisallowMovesTests(unittest.TestCase):

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

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromA3ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(A3, H8))

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromH3ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(H3, A8))

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromH1ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.queen, self.testUtility.getMove(H1, E5)),
                                            F4)

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromB2ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(B2, A8))

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromC3ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.queen, self.testUtility.getMove(C3, A8))

    def testfailToMoveButValidMoveOnNewBoardWhiteQueenFromA1ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.queen, self.testUtility.getMove(A1, D5)),
                                            F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromA2ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(A2, H8))

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromE5ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(E5, A8))

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromD8ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(D8, E5)),
            F4)

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromF7ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(F7, A8))

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromD2ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(D2, A8))

    def testfailToMoveButValidMoveOnNewBoardBlackQueenFromA1ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.queen, self.testUtility.getMove(A1, D5)),
            F5)
