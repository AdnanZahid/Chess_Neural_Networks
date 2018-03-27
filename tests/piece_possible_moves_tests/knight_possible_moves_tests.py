from tests.test_utils.test_utility import *


# This class tests if knight legal moves are blocked as intended
class KnightPossibleMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testPossibleMovesWhiteKnightFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.knight, A1))
        comparisonMoves = [B3, C2]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKnightFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.knight, D5))
        comparisonMoves = [E7, F6, C7, B6, E3, F4, C3, B4]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKnightFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.knight, E6)
        self.testUtility.moveValueToSquare(Values.knight, E2)
        self.testUtility.moveValueToSquare(Values.knight, F5)
        self.testUtility.moveValueToSquare(Values.knight, F3)
        self.testUtility.moveValueToSquare(Values.knight, C6)
        self.testUtility.moveValueToSquare(Values.knight, C2)
        self.testUtility.moveValueToSquare(Values.knight, B5)
        self.testUtility.moveValueToSquare(Values.knight, B3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.knight, D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKnightFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.knight, E6)
        self.testUtility.moveValueToSquare(-Values.knight, E2)
        self.testUtility.moveValueToSquare(-Values.knight, F5)
        self.testUtility.moveValueToSquare(-Values.knight, F3)
        self.testUtility.moveValueToSquare(-Values.knight, C6)
        self.testUtility.moveValueToSquare(-Values.knight, C2)
        self.testUtility.moveValueToSquare(-Values.knight, B5)
        self.testUtility.moveValueToSquare(-Values.knight, B3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.knight, D4))
        comparisonMoves = [E6, E2, F5, F3, C6, C2, B5, B3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackKnightFromH1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.knight, H1))
        comparisonMoves = [G3, F2]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKnightFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.knight, E4))
        comparisonMoves = [F6, G5, D6, C5, F2, G3, D2, C3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKnightFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.knight, F8)
        self.testUtility.moveValueToSquare(-Values.knight, F4)
        self.testUtility.moveValueToSquare(-Values.knight, G7)
        self.testUtility.moveValueToSquare(-Values.knight, G5)
        self.testUtility.moveValueToSquare(-Values.knight, D8)
        self.testUtility.moveValueToSquare(-Values.knight, D4)
        self.testUtility.moveValueToSquare(-Values.knight, C7)
        self.testUtility.moveValueToSquare(-Values.knight, C5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.knight, E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKnightFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.knight, F8)
        self.testUtility.moveValueToSquare(Values.knight, F4)
        self.testUtility.moveValueToSquare(Values.knight, G7)
        self.testUtility.moveValueToSquare(Values.knight, G5)
        self.testUtility.moveValueToSquare(Values.knight, D8)
        self.testUtility.moveValueToSquare(Values.knight, D4)
        self.testUtility.moveValueToSquare(Values.knight, C7)
        self.testUtility.moveValueToSquare(Values.knight, C5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.knight, E6))
        comparisonMoves = [F8, F4, G7, G5, D8, D4, C7, C5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
