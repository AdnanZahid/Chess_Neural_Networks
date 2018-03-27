from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are blocked as intended
class BishopPossibleMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testPossibleMovesWhiteBishopFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.bishop, A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteBishopFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.bishop, D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteBishopFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.bishop, E5)
        self.testUtility.moveValueToSquare(Values.bishop, E3)
        self.testUtility.moveValueToSquare(Values.bishop, C5)
        self.testUtility.moveValueToSquare(Values.bishop, C3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.bishop, D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteBishopFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, E5)
        self.testUtility.moveValueToSquare(-Values.bishop, E3)
        self.testUtility.moveValueToSquare(-Values.bishop, C5)
        self.testUtility.moveValueToSquare(-Values.bishop, C3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.bishop, D4))
        comparisonMoves = [E5, E3, C5, C3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackBishopFromH1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.bishop, H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackBishopFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.bishop, E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackBishopFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.bishop, F7)
        self.testUtility.moveValueToSquare(-Values.bishop, F5)
        self.testUtility.moveValueToSquare(-Values.bishop, D7)
        self.testUtility.moveValueToSquare(-Values.bishop, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.bishop, E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackBishopFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.bishop, F7)
        self.testUtility.moveValueToSquare(Values.bishop, F5)
        self.testUtility.moveValueToSquare(Values.bishop, D7)
        self.testUtility.moveValueToSquare(Values.bishop, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.bishop, E6))
        comparisonMoves = [F7, F5, D7, D5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
