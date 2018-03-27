from tests.test_utils.test_utility import *


# This class tests if knight legal moves are allowed as intended
class KnightAllowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.knight, self.testUtility.getMove(A1, C2))

    def testMoveWhiteKnightFromG7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.knight, self.testUtility.getMove(G7, F5))

    def testMoveWhiteKnightFromD4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(self.testUtility.move(Values.knight, self.testUtility.getMove(D4, F5)),
                                           E3)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackKnightFromA1ToC2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.knight, self.testUtility.getMove(A1, C2))

    def testMoveBlackKnightFromG7ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.knight, self.testUtility.getMove(G7, F5))

    def testMoveBlackKnightFromD4ToF5ToE3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(self.testUtility.move(-Values.knight, self.testUtility.getMove(D4, F5)),
                                           E3)
