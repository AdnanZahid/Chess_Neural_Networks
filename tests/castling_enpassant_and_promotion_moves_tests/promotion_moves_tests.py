from tests.test_utils.test_utility import *


# This class tests if legal promotion moves are possible as intended
class PromotionMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        # These 3 methods will wipe the slate clean so we can begin anew
        self.board.setupEmptyBoard()
        self.gameLogic.whitePlayer.clearPlayerData()
        self.gameLogic.blackPlayer.clearPlayerData()

    def checkIfPromotionIsSuccessful(self, pawn):
        self.assertTrue(pawn.__class__ == Queen)
        self.assertTrue(pawn.value == Values.queen)
        self.assertTrue(pawn.directionsList == [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)])
        if pawn.color == Color.white:
            self.assertTrue(pawn.symbol == Symbols.white_queen)
        else:
            self.assertTrue(pawn.symbol == Symbols.black_queen)

    # ///////////
    # // WHITE //
    # ///////////

    def testWhitePromotionFromA7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # 1. a8q
        # Move white pawn on A7 to A8 (promote to queen)
        whitePawn = self.testUtility.move(Values.pawn, self.testUtility.getMove(A7, A8))
        # Check if successfully promoted to queen
        self.checkIfPromotionIsSuccessful(whitePawn)

    def testWhitePromotionFromD2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # 1. d4 h6
        # 2. d5 h5
        # 3. d6 h4
        # 4. d7 h3
        # 5. d8q

        # Move white pawn on D2 to D4
        whitePawn = self.testUtility.move(Values.pawn, self.testUtility.getMove(D2, D4))
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H7 to H6
        blackPawn = self.testUtility.move(-Values.pawn, self.testUtility.getMove(H7, H6))
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D2 to D4
        self.testUtility.moveToSquare(whitePawn, D5)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H6 to H5
        self.testUtility.moveToSquare(blackPawn, H5)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D5 to D6
        self.testUtility.moveToSquare(whitePawn, D6)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H5 to H4
        self.testUtility.moveToSquare(blackPawn, H4)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D6 to D7
        self.testUtility.moveToSquare(whitePawn, D7)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H4 to H3
        self.testUtility.moveToSquare(blackPawn, H3)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D7 to D8 (promote to queen)
        self.testUtility.moveToSquare(whitePawn, D8)
        # Check if successfully promoted to queen
        self.checkIfPromotionIsSuccessful(whitePawn)

    def testWhitePromotionFromH5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # 1. h6 a4
        # 2. h7 a3
        # 3. h8q

        # Move white pawn on H5 to H6
        whitePawn = self.testUtility.move(Values.pawn, self.testUtility.getMove(H5, H6))
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A5 to A4
        blackPawn = self.testUtility.move(-Values.pawn, self.testUtility.getMove(A5, A4))
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on H6 to H7
        self.testUtility.moveToSquare(whitePawn, H7)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A4 to A3
        self.testUtility.moveToSquare(blackPawn, A3)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on H7 to H8 (promote to queen)
        self.testUtility.moveToSquare(whitePawn, H8)
        # Check if successfully promoted to queen
        self.checkIfPromotionIsSuccessful(whitePawn)

    # ///////////
    # // BLACK //
    # ///////////

    def testBlackPromotionFromA7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # 1. d4 a6
        # 2. d5 a5
        # 3. d6 a4
        # 4. d7 a3
        # 5. d8q a2
        # 6. qd7 a1q

        # Move white pawn on D2 to D4
        whitePawn = self.testUtility.move(Values.pawn, self.testUtility.getMove(D2, D4))
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A7 to A6
        blackPawn = self.testUtility.move(-Values.pawn, self.testUtility.getMove(A7, A6))
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D2 to D4
        self.testUtility.moveToSquare(whitePawn, D5)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A6 to A5
        self.testUtility.moveToSquare(blackPawn, A5)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D5 to D6
        self.testUtility.moveToSquare(whitePawn, D6)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A5 to A4
        self.testUtility.moveToSquare(blackPawn, A4)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D6 to D7
        self.testUtility.moveToSquare(whitePawn, D7)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A4 to A3
        self.testUtility.moveToSquare(blackPawn, A3)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D7 to D8 (promote to queen)
        self.testUtility.moveToSquare(whitePawn, D8)
        # Check if white pawn successfully promoted to queen
        self.checkIfPromotionIsSuccessful(whitePawn)
        whiteQueen = whitePawn
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A3 to A2
        self.testUtility.moveToSquare(blackPawn, A2)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white queen on D8 to D7
        self.testUtility.moveToSquare(whiteQueen, D7)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on A2 to A1
        self.testUtility.moveToSquare(blackPawn, A1)
        # Check if black pawn successfully promoted to queen
        self.checkIfPromotionIsSuccessful(blackPawn)

    def testBlackPromotionFromD2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # 1. nothing (white) d2q (black)
        # Move black pawn on D2 to D1 (promote to queen)
        blackPawn = self.testUtility.move(-Values.pawn, self.testUtility.getMove(D2, D1))
        # Check if successfully promoted to queen
        self.checkIfPromotionIsSuccessful(blackPawn)

    def testBlackPromotionFromH5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # 1. d4 h4
        # 2. d5 h3
        # 3. d6 h2
        # 4. d7 h1q

        # Move white pawn on D2 to D4
        whitePawn = self.testUtility.move(Values.pawn, self.testUtility.getMove(D2, D4))
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H5 to H4
        blackPawn = self.testUtility.move(-Values.pawn, self.testUtility.getMove(H5, H4))
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D4 to D5
        self.testUtility.moveToSquare(whitePawn, D5)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H4 to H3
        self.testUtility.moveToSquare(blackPawn, H3)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D5 to D6
        self.testUtility.moveToSquare(whitePawn, D6)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H3 to H2
        self.testUtility.moveToSquare(blackPawn, H2)
        # Change turn to white player
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        # Move white pawn on D6 to D7
        self.testUtility.moveToSquare(whitePawn, D7)
        # Change turn to black player
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        # Move black pawn on H2 to H1 (promote to queen)
        self.testUtility.moveToSquare(blackPawn, H1)
        # Check if black pawn successfully promoted to queen
        self.checkIfPromotionIsSuccessful(blackPawn)
