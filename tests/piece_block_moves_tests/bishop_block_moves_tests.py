from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are blocked as intended
class BishopBlockMovesTests(unittest.TestCase):

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

    def testBlockWhiteBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.bishop, H8)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.bishop, self.testUtility.getMove(A1, H8))

    def testBlockWhiteBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.bishop, D5)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.bishop, self.testUtility.getMove(H1, A8))

    def testBlockWhiteBishopFromD4ToE5ToC3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.bishop, E5)
        self.testUtility.moveValueToSquare(Values.bishop, C3)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(Values.bishop, \
                                             self.testUtility.getMove(D4, E5)), C3)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlockBlackBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, D4)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.bishop, self.testUtility.getMove(A1, H8))

    def testBlockBlackBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, D5)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.bishop, self.testUtility.getMove(H1, A8))

    def testBlockBlackBishopFromD4ToE5ToC3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, E5)
        self.testUtility.moveValueToSquare(-Values.bishop, C3)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.bishop, \
                                             self.testUtility.getMove(D4, E5)), C3)
