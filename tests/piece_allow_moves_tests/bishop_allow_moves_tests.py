from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are allowed as intended
class BishopAllowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.bishop, self.testUtility.getMove(A1, H8))

    def testMoveWhiteBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.bishop, self.testUtility.getMove(H1, A8))

    def testMoveWhiteBishopFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(self.testUtility.move(Values.bishop, self.testUtility.getMove(D4, E5)),
                                           F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackBishopFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.bishop, self.testUtility.getMove(A1, H8))

    def testMoveBlackBishopFromH1ToA8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.bishop, self.testUtility.getMove(H1, A8))

    def testMoveBlackBishopFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(self.testUtility.move(-Values.bishop, self.testUtility.getMove(D4, E5)),
                                           F4)
