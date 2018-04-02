from tests.test_utils.test_utility import *


# This class tests if queen legal moves are blocked as intended
class QueenBlockMovesTests(unittest.TestCase):

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

    def testBlockWhiteQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, H8)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, self.testUtility.getMove(A1, H8))

    def testBlockWhiteQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, self.testUtility.getMove(H1, A8))

    def testBlockWhiteQueenFromD4ToE5ToF6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, F6)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, \
                                             self.testUtility.getMove(D4, E5)), F6)

    def testBlockWhiteQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, A8)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, self.testUtility.getMove(A1, A8))

    def testBlockWhiteQueenFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, A1)
        self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, self.testUtility.getMove(H1, A1))

    def testBlockWhiteQueenFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, E4)
        self.testUtility.moveValueToSquare(Values.queen, F4)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(Values.queen, \
                                             self.testUtility.getMove(D4, E4)), F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlockBlackQueenFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, D4)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, self.testUtility.getMove(A1, H8))

    def testBlockBlackQueenFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, self.testUtility.getMove(H1, A8))

    def testBlockBlackQueenFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, F4)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, \
                                             self.testUtility.getMove(D4, E5)), F4)

    def testBlockBlackQueenFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A8)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, self.testUtility.getMove(A1, A8))

    def testBlockBlackQueenFromH1ToA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, A1)
        self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, self.testUtility.getMove(H1, A1))

    def testBlockBlackQueenFromD4ToE4ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E4)
        self.testUtility.moveValueToSquare(-Values.queen, F4)
        self.testUtility.invalidMoveButValidOnNewBoard( \
            self.testUtility.failToMoveButValidMoveOnNewBoard(-Values.queen, \
                                             self.testUtility.getMove(D4, E4)), F4)
