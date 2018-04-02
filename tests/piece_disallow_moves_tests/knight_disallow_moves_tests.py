from tests.test_utils.test_utility import *


# This class tests if knight legal moves are disallowed as intended
class KnightDisallowMovesTests(unittest.TestCase):

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

    def testfailToMoveButValidMoveOnNewBoardWhiteKnightFromG1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(G1, C2))

    def testfailToMoveButValidMoveOnNewBoardWhiteKnightFromB7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.knight, self.testUtility.getMove(B7, F5))

    def testfailToMoveButValidMoveOnNewBoardWhiteKnightFromA4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(Values.knight, self.testUtility.getMove(A4, F5)),
            E3)

    # ///////////
    # // BLACK //
    # ///////////

    def testfailToMoveButValidMoveOnNewBoardBlackKnightFromH1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(H1, C2))

    def testfailToMoveButValidMoveOnNewBoardBlackKnightFromA7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(A7, F5))

    def testfailToMoveButValidMoveOnNewBoardBlackKnightFromA4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(
            self.testUtility.failToMove(-Values.knight, self.testUtility.getMove(A4, F5)),
            E3)
