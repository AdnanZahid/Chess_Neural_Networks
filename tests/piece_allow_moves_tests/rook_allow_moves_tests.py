from tests.test_utils.test_utility import *


# This class tests if rook legal moves are allowed as intended
class RookAllowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.rook, self.testUtility.getMove(A1, A8))

    def testMoveWhiteRookFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.rook, self.testUtility.getMove(H8, A8))

    def testMoveWhiteRookFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(self.testUtility.move(Values.rook, self.testUtility.getMove(D4, D5)),
                                           F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackRookFromA1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.rook, self.testUtility.getMove(A1, A8))

    def testMoveBlackRookFromH8ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.rook, self.testUtility.getMove(H8, A8))

    def testMoveBlackRookFromD4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(self.testUtility.move(-Values.rook, self.testUtility.getMove(D4, D5)),
                                           F5)
