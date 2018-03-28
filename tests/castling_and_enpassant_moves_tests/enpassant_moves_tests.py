from tests.test_utils.test_utility import *


# This class tests if legal enpassant moves are possible as intended
class EnpassantMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testEnpassantWhiteCapturesBlackOnA6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, B5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(A7, A5))
        self.testUtility.moveToSquare(whiteBPawn, A6)

    def testEnpassantWhiteCapturesBlackOnE6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, D5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(E7, E5))
        self.testUtility.moveToSquare(whiteBPawn, E6)

    def testEnpassantWhiteCapturesBlackOnH6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, G5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(H7, H5))
        self.testUtility.moveToSquare(whiteBPawn, H6)

    # ///////////
    # // BLACK //
    # ///////////

    def testEnpassantBlackCapturesWhiteOnA3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(-Values.pawn, B4)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(A2, A4))
        self.testUtility.moveToSquare(whiteBPawn, A3)

    def testEnpassantBlackCapturesWhiteOnD3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(-Values.pawn, C4)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(D2, D4))
        self.testUtility.moveToSquare(whiteBPawn, D3)

    def testEnpassantBlackCapturesWhiteOnH3(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(-Values.pawn, G4)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(H2, H4))
        self.testUtility.moveToSquare(whiteBPawn, H3)
