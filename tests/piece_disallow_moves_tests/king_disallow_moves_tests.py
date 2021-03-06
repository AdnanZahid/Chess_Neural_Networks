from tests.test_utils.test_utility import *


# This class tests if king legal moves are disallowed as intended
class KingDisallowMovesTests(unittest.TestCase):

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

    def testfailToMoveButValidMoveOnNewBoardWhiteKingFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(A1, C2))

    def testfailToMoveButValidMoveOnNewBoardWhiteKingFromG7ToB8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(G7, B8))

    def testfailToMoveButValidMoveOnNewBoardWhiteKingFromA4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.king, self.testUtility.getMove(A4, E5)),
                                            F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testfailToMoveButValidMoveOnNewBoardBlackKingFromD1ToB2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(D1, B2))

    def testfailToMoveButValidMoveOnNewBoardBlackKingFromA7ToG8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(A7, G8))

    def testfailToMoveButValidMoveOnNewBoardBlackKingFromA4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.king, self.testUtility.getMove(A4, E5)),
                                            F4)
