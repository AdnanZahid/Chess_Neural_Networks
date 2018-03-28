from tests.test_utils.test_utility import *


# This class tests if legal castling moves are possible as intended
class CastlingMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.performCastlingSetup()

    # ///////////
    # // WHITE //
    # ///////////

    # def testWhiteCastleKingSide(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
    #     king = self.testUtility.moveValueToSquare(Values.king, E1)
    #     self.testUtility.moveToSquare(king, G1)
    #
    # def testWhiteCastleQueenSide(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
    #     king = self.testUtility.moveValueToSquare(Values.king, E1)
    #     self.testUtility.moveToSquare(king, C1)
    #
    # def testWhiteCastleKingSideInvalid(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
    #     king = self.testUtility.moveValueToSquare(Values.king, E1)
    #     self.testUtility.moveValueToSquare(Values.knight, G1)
    #     self.testUtility.failToMoveToSquare(king, G1)
    #
    # def testWhiteCastleQueenSideInvalid(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
    #     king = self.testUtility.moveValueToSquare(Values.king, E1)
    #     self.testUtility.moveValueToSquare(-Values.knight, D1)
    #     self.testUtility.failToMoveToSquare(king, C1)

    # ///////////
    # // BLACK //
    # ///////////

    # def testBlackCastleKingSide(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
    #     king = self.testUtility.moveValueToSquare(-Values.king, E8)
    #     self.testUtility.moveToSquare(king, G8)
    #
    # def testBlackCastleQueenSide(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
    #     king = self.testUtility.moveValueToSquare(-Values.king, E8)
    #     self.testUtility.moveToSquare(king, C8)
    #
    # def testBlackCastleKingSideInvalid(self):
    #     self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
    #     king = self.testUtility.moveValueToSquare(-Values.king, E8)
    #     self.testUtility.moveValueToSquare(-Values.bishop, F8)
    #     self.testUtility.failToMoveToSquare(king, G8)

    def testBlackCastleQueenSideInvalid(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        king = self.testUtility.moveValueToSquare(-Values.king, E8)
        self.testUtility.moveValueToSquare(Values.knight, C8)
        self.testUtility.failToMoveToSquare(king, C8)

    def performCastlingSetup(self):
        # Take away white pieces in the way of castling
        # Put empty piece on B1
        self.assertTrue(self.board.putEmptyPieceOnPosition(B1))
        # Put empty piece on C1
        self.assertTrue(self.board.putEmptyPieceOnPosition(C1))
        # Put empty piece on D1
        self.assertTrue(self.board.putEmptyPieceOnPosition(D1))
        # Put empty piece on F1
        self.assertTrue(self.board.putEmptyPieceOnPosition(F1))
        # Put empty piece on G1
        self.assertTrue(self.board.putEmptyPieceOnPosition(G1))

        # Take away black pieces in the way of castling
        # Put empty piece on B8
        self.assertTrue(self.board.putEmptyPieceOnPosition(B8))
        # Put empty piece on C8
        self.assertTrue(self.board.putEmptyPieceOnPosition(C8))
        # Put empty piece on D8
        self.assertTrue(self.board.putEmptyPieceOnPosition(D8))
        # Put empty piece on F8
        self.assertTrue(self.board.putEmptyPieceOnPosition(F8))
        # Put empty piece on G8
        self.assertTrue(self.board.putEmptyPieceOnPosition(G8))
