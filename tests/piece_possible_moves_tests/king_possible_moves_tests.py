from tests.test_utils.test_utility import *


# This class tests if king legal moves are blocked as intended
class KingPossibleMovesTests(unittest.TestCase):

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

    def testPossibleMovesWhiteKingFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.king, A1))
        comparisonMoves = [B2, B1, A2]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKingFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.king, D5))
        comparisonMoves = [E6, E4, C6, C4, E5, D6, C5, D4]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKingFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, E4)
        self.testUtility.moveValueToSquare(Values.queen, E3)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.moveValueToSquare(Values.queen, D3)
        self.testUtility.moveValueToSquare(Values.queen, C5)
        self.testUtility.moveValueToSquare(Values.queen, C4)
        self.testUtility.moveValueToSquare(Values.queen, C3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.king, D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteKingFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, E4)
        self.testUtility.moveValueToSquare(-Values.queen, E3)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.moveValueToSquare(-Values.queen, D3)
        self.testUtility.moveValueToSquare(-Values.queen, C5)
        self.testUtility.moveValueToSquare(-Values.queen, C4)
        self.testUtility.moveValueToSquare(-Values.queen, C3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.king, D4))
        comparisonMoves = [E5, E3, C5, C3, E4, D5, C4, D3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackKingFromH1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.king, H1))
        comparisonMoves = [G2, H2, G1]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKingFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.king, E4))
        comparisonMoves = [F5, F3, D5, D3, F4, E5, D4, E3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKingFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, F7)
        self.testUtility.moveValueToSquare(-Values.queen, F6)
        self.testUtility.moveValueToSquare(-Values.queen, F5)
        self.testUtility.moveValueToSquare(-Values.queen, E7)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, D7)
        self.testUtility.moveValueToSquare(-Values.queen, D6)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.king, E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackKingFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, F7)
        self.testUtility.moveValueToSquare(Values.queen, F6)
        self.testUtility.moveValueToSquare(Values.queen, F5)
        self.testUtility.moveValueToSquare(Values.queen, E7)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, D7)
        self.testUtility.moveValueToSquare(Values.queen, D6)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.king, E6))
        comparisonMoves = [F7, F5, D7, D5, F6, E7, D6, E5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
