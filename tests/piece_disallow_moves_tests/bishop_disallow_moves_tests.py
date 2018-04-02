from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are disallowed as intended
class BishopDisallowMovesTests(unittest.TestCase):

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

    def testfailToMoveButValidMoveOnNewBoardWhiteBishopFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(A1, A8))

    def testfailToMoveButValidMoveOnNewBoardWhiteBishopFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(H1, A1))

    def testfailToMoveButValidMoveOnNewBoardWhiteBishopFromD4ToD5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(Values.bishop, self.testUtility.getMove(D4, D5)),
            F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testfailToMoveButValidMoveOnNewBoardBlackBishopFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(A1, A8))

    def testfailToMoveButValidMoveOnNewBoardBlackBishopFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(H1, A1))

    def testfailToMoveButValidMoveOnNewBoardBlackBishopFromD4ToD5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.bishop, self.testUtility.getMove(D4, D5)),
            F4)
