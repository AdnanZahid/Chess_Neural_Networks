from tests.test_utils.test_utility import *


# This class tests if queen legal moves are blocked as intended
class QueenPossibleMovesTests(unittest.TestCase):

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

    def testPossibleMovesWhiteQueenFromA1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.queen, A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8, B1, C1, D1, E1, F1, G1, H1, A2, A3, A4, A5, A6, A7, A8]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteQueenFromD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.queen, D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2, D1, D2, D3, D4, D6, D7, D8, A5, B5, C5,
                           E5, F5, G5, H5]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteQueenFromD4FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, E3)
        self.testUtility.moveValueToSquare(Values.queen, C5)
        self.testUtility.moveValueToSquare(Values.queen, C3)
        self.testUtility.moveValueToSquare(Values.queen, E4)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.moveValueToSquare(Values.queen, C4)
        self.testUtility.moveValueToSquare(Values.queen, D3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.queen, D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesWhiteQueenFromD4EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, E3)
        self.testUtility.moveValueToSquare(-Values.queen, C5)
        self.testUtility.moveValueToSquare(-Values.queen, C3)
        self.testUtility.moveValueToSquare(-Values.queen, E4)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.moveValueToSquare(-Values.queen, C4)
        self.testUtility.moveValueToSquare(-Values.queen, D3)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(Values.queen, D4))
        comparisonMoves = [E5, E3, C5, C3, E4, D5, C4, D3]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    # ///////////
    # // BLACK //
    # ///////////

    def testPossibleMovesBlackQueenFromH1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.queen, H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8, H2, H3, H4, H5, H6, H7, H8, G1, F1, E1, D1, C1, B1, A1]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackQueenFromE4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.queen, E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1, E1, E2, E3, E5, E6, E7, E8, A4, B4, C4,
                           D4, F4, G4, H4]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackQueenFromDE6FriendlyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.queen, F7)
        self.testUtility.moveValueToSquare(-Values.queen, F5)
        self.testUtility.moveValueToSquare(-Values.queen, D7)
        self.testUtility.moveValueToSquare(-Values.queen, D5)
        self.testUtility.moveValueToSquare(-Values.queen, D6)
        self.testUtility.moveValueToSquare(-Values.queen, E7)
        self.testUtility.moveValueToSquare(-Values.queen, E5)
        self.testUtility.moveValueToSquare(-Values.queen, F6)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.queen, E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)

    def testPossibleMovesBlackQueenFromDE6EnemyFire(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(Values.queen, F7)
        self.testUtility.moveValueToSquare(Values.queen, F5)
        self.testUtility.moveValueToSquare(Values.queen, D7)
        self.testUtility.moveValueToSquare(Values.queen, D5)
        self.testUtility.moveValueToSquare(Values.queen, D6)
        self.testUtility.moveValueToSquare(Values.queen, E7)
        self.testUtility.moveValueToSquare(Values.queen, E5)
        self.testUtility.moveValueToSquare(Values.queen, F6)
        possibleMoves = self.testUtility.generateAllPossibleTargetSquares(
            self.testUtility.moveValueToSquare(-Values.queen, E6))
        comparisonMoves = [F7, F5, D7, D5, D6, E7, E5, F6]
        self.testUtility.checkEqualMoves(possibleMoves, comparisonMoves)
