from tests.test_utils.test_utility import *


# This class tests if rook legal moves are blocked as intended
class RookPossibleMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testPossibleMovesWhiteRookFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.rook, A1))
        comparisonMoves = [B1, C1, D1, E1, F1, G1, H1, A2, A3, A4, A5, A6, A7, A8]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteRookFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.rook, D5))
        comparisonMoves = [D1, D2, D3, D4, D6, D7, D8, A5, B5, C5, E5, F5, G5, H5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteRookFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.rook, E4)
        self.testUtility.moveValueToSquare(Values.rook, D5)
        self.testUtility.moveValueToSquare(Values.rook, C4)
        self.testUtility.moveValueToSquare(Values.rook, D3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.rook, D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteRookFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.rook, E4)
        self.testUtility.moveValueToSquare(-Values.rook, D5)
        self.testUtility.moveValueToSquare(-Values.rook, C4)
        self.testUtility.moveValueToSquare(-Values.rook, D3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.rook, D4))
        comparisonMoves = [E4, D5, C4, D3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackRookFromH1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.rook, H1))
        comparisonMoves = [H2, H3, H4, H5, H6, H7, H8, G1, F1, E1, D1, C1, B1, A1]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackRookFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.rook, E4))
        comparisonMoves = [E1, E2, E3, E5, E6, E7, E8, A4, B4, C4, D4, F4, G4, H4]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackRookFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.rook, D6)
        self.testUtility.moveValueToSquare(-Values.rook, E7)
        self.testUtility.moveValueToSquare(-Values.rook, E5)
        self.testUtility.moveValueToSquare(-Values.rook, F6)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.rook, E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackRookFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.rook, D6)
        self.testUtility.moveValueToSquare(Values.rook, E7)
        self.testUtility.moveValueToSquare(Values.rook, E5)
        self.testUtility.moveValueToSquare(Values.rook, F6)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.rook, E6))
        comparisonMoves = [D6, E7, E5, F6]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
