from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are blocked as intended
class PawnPossibleMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    # ///////////
    # // WHITE //
    # ///////////

    def testPossibleMovesWhitePawnFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        piece = self.testUtility.moveValueToSquare(Values.pawn, A2)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [A3, A4]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhitePawnFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        piece = self.testUtility.moveValueToSquare(Values.pawn, D5)
        piece.hasMoved = True
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [D6]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhitePawnFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        piece = self.testUtility.moveValueToSquare(Values.pawn, D4)
        self.testUtility.moveValueToSquare(Values.pawn, E5)
        self.testUtility.moveValueToSquare(Values.pawn, D5)
        self.testUtility.moveValueToSquare(Values.pawn, C5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhitePawnFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        piece = self.testUtility.moveValueToSquare(Values.pawn, D4)
        self.testUtility.moveValueToSquare(-Values.pawn, E5)
        self.testUtility.moveValueToSquare(-Values.pawn, D5)
        self.testUtility.moveValueToSquare(-Values.pawn, C5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [E5, C5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackPawnFromH7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        piece = self.testUtility.moveValueToSquare(-Values.pawn, H7)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [H6, H5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackPawnFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        piece = self.testUtility.moveValueToSquare(-Values.pawn, E4)
        piece.hasMoved = True
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [E3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackPawnFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        piece = self.testUtility.moveValueToSquare(-Values.pawn, E6)
        self.testUtility.moveValueToSquare(-Values.pawn, F5)
        self.testUtility.moveValueToSquare(-Values.pawn, E5)
        self.testUtility.moveValueToSquare(-Values.pawn, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackPawnFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        piece = self.testUtility.moveValueToSquare(-Values.pawn, E6)
        self.testUtility.moveValueToSquare(Values.pawn, F5)
        self.testUtility.moveValueToSquare(Values.pawn, E5)
        self.testUtility.moveValueToSquare(Values.pawn, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(piece)
        comparisonMoves = [F5, D5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
