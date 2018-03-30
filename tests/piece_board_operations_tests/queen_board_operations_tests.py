from tests.test_utils.test_utility import *


# This class tests if queen legal moves are blocked as intended
class QueenBoardOperationsTests(unittest.TestCase):

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

    def testGetWhiteQueenOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.isPieceExists(Values.queen, D4)

    def testPutWhiteQueenOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testGetBlackQueenOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.isPieceExists(-Values.queen, D4)

    def testPutBlackQueenOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, D4)
