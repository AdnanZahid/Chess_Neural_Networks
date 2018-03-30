from tests.test_utils.test_utility import *


# This class tests if legal enpassant moves are possible as intended
class EnpassantMovesTests(unittest.TestCase):

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

    def testEnpassantWhiteCapturesBlackOnA6(self):
        # Assigning black player (only in this case since black has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, B5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(A7, A5))
        # Changing turn back to white
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(whiteBPawn, A6)

    def testEnpassantWhiteCapturesBlackOnE6(self):
        # Assigning black player (only in this case since black has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, D5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(E7, E5))
        # Changing turn back to white
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(whiteBPawn, E6)

    def testEnpassantWhiteCapturesBlackOnH6(self):
        # Assigning black player (only in this case since black has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        whiteBPawn = self.testUtility.moveValueToSquare(Values.pawn, G5)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(H7, H5))
        # Changing turn back to white
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(whiteBPawn, H6)

    # ///////////
    # // BLACK //
    # ///////////

    def testEnpassantBlackCapturesWhiteOnA3(self):
        # Assigning white player (only in this case since white has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        blackBPawn = self.testUtility.moveValueToSquare(-Values.pawn, B4)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(A2, A4))
        # Changing turn back to black
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(blackBPawn, A3)

    def testEnpassantBlackCapturesWhiteOnD3(self):
        # Assigning white player (only in this case since white has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        blackBPawn = self.testUtility.moveValueToSquare(-Values.pawn, C4)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(D2, D4))
        # Changing turn back to black
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(blackBPawn, D3)

    def testEnpassantBlackCapturesWhiteOnH3(self):
        # Assigning white player (only in this case since white has to move first for enpassant)
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        blackBPawn = self.testUtility.moveValueToSquare(-Values.pawn, G4)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(H2, H4))
        # Changing turn back to black
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(blackBPawn, H3)
