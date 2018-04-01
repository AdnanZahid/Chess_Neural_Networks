from tests.test_utils.test_utility import *


# This class tests if player logic is working properly
class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.whitePlayer = self.gameLogic.whitePlayer
        self.blackPlayer = self.gameLogic.blackPlayer
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)

    def testMove(self):
        # Move white knight on B1 to C3
        self.move(B1, C3)
        # Move black knight on B8 to A6
        self.move(G8, F6)

    def testSetKing(self):
        self.assertTrue(self.whitePlayer.king == self.board.getPieceOnPosition(E1))
        self.assertTrue(self.blackPlayer.king == self.board.getPieceOnPosition(E8))

    def setKingSideRook(self):
        self.assertTrue(self.whitePlayer.kingSideRook == self.board.getPieceOnPosition(H1))
        self.assertTrue(self.blackPlayer.kingSideRook == self.board.getPieceOnPosition(H8))

    def setQueenSideRook(self):
        self.assertTrue(self.whitePlayer.queenSideRook == self.board.getPieceOnPosition(A1))
        self.assertTrue(self.blackPlayer.queenSideRook == self.board.getPieceOnPosition(A8))

    def testGetAllPossibleTargetSquares(self):
        self.testUtility.checkEqualMoves(self.whitePlayer.getAllPossibleTargetSquares(self.board),
                                         [A3, B3, C3, D3, E3, F3, G3, H3,
                                          A4, B4, C4, D4, E4, F4, G4, H4])

        self.gameLogic.changeTurn()

        self.testUtility.checkEqualMoves(self.blackPlayer.getAllPossibleTargetSquares(self.board),
                                         [A6, B6, C6, D6, E6, F6, G6, H6,
                                          A5, B5, C5, D5, E5, F5, G5, H5])

    def testIsUnderCheck(self):
        # First see if white king is under check (it should not be)
        self.assertFalse(self.whitePlayer.isUnderCheck(self.board))
        # Perform fool's mate on white
        self.getCheckOnWhite()
        # Now check if white king is under check
        self.assertTrue(self.whitePlayer.isUnderCheck(self.board))

    def testIsUnderCheckMate(self):
        # First see if white king is under checkmate (it should not be)
        self.assertFalse(self.whitePlayer.isUnderCheckMate(self.board))
        # Perform fool's mate on white
        self.performFoolsMateOnWhite()
        # Now check if white king is under checkmate
        self.assertTrue(self.whitePlayer.isUnderCheckMate(self.board))

    def testCaptureWhiteQueenThatHasEnteredBlacksCampByRook(self):
        # Infilterate blacks camp with white queen (and get captured)
        self.infilterateBlacksCampWithWhiteQueen()
        # Capture white's queen on D8 by black's rook on F8
        self.assertTrue(self.move(F8, D8))

    def testCaptureWhiteQueenThatHasEnteredBlacksCampByBishopAfterItCapturesTheRook(self):
        # Infilterate blacks camp with white queen (and get captured)
        self.infilterateBlacksCampWithWhiteQueen()
        # Move black pawn on A7 to A6
        self.assertTrue(self.move(A7, A6))
        # Move white queen on D8 to F8
        self.assertTrue(self.move(D8, F8))
        # Now check if black bishop on C5 can move at all
        self.assertFalse(MoveGenerator.generatePossibleTargetSquares(self.board.getPieceOnPosition(C5), self.board, self.blackPlayer) == [])

    def testBlockWhiteQueenThatHasEnteredBlacksCampByKnightAfterItCapturesTheRook(self):
        # Infilterate blacks camp with white queen (and get captured)
        self.infilterateBlacksCampWithWhiteQueen()
        # Move black pawn on F8 to E8
        self.assertTrue(self.move(F8, E8))
        # Move white queen on D8 to E8
        self.assertTrue(self.move(D8, E8))
        # Now check if black king is under checkmate (it should fail)
        self.assertFalse(self.blackPlayer.isUnderCheckMate(self.board))

    def testTrytoMoveWhileInCheckVariation1(self):
        # 1. f3 e5
        # 2. g4 Qh4#
        # 3. a3 will fail
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white pawn on G2 to G4
        self.assertTrue(self.move(G2, G4))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))
        # Move white pawn on A2 to A3 (will fail)
        self.assertFalse(self.move(A2, A3))

    def testTrytoMoveWhileInCheckVariation2(self):
        # Infilterate blacks camp with white queen (and get captured)
        self.infilterateBlacksCampWithWhiteQueen()
        # Move black pawn from A7 to A6
        self.assertTrue(self.move(A7, A6))
        # Move white queen from D8 to F8
        self.assertTrue(self.move(D8, F8))
        # Move black pawn from A6 to A5 (will fail)
        self.assertFalse(self.move(A6, A5))

    def testBlockWhileInCheck(self):
        # 1. f3 e5
        # 2. g1 -> h3 Qh4#
        # 3. g3 will pass
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white knight on G1 to H3
        self.assertTrue(self.move(G1, H3))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))
        # Now check if white king is under check (it should be)
        self.assertTrue(self.whitePlayer.isUnderCheck(self.board))
        # Now check if white king is under checkmate (it should not be)
        self.assertFalse(self.whitePlayer.isUnderCheckMate(self.board))
        # Move white pawn on G2 to G3
        self.assertTrue(self.move(G2, G3))
        # Now check if white king is under check (it should not be)
        self.assertFalse(self.whitePlayer.isUnderCheck(self.board))

    def move(self, fromSquare, toSquare):
        piece = self.board.getPieceOnPosition(fromSquare)
        self.gameLogic.move(EvaluationMove(piece.position, toSquare))
        return piece.position == toSquare

    def getCheckOnWhite(self):
        # 1. f3 e5
        # 2. g1 -> h3 Qh4#
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white knight on G1 to H3
        self.assertTrue(self.move(G1, H3))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))

    def performFoolsMateOnWhite(self):
        # 1. f3 e5
        # 2. g4 Qh4#
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white pawn on G2 to G4
        self.assertTrue(self.move(G2, G4))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))

    def infilterateBlacksCampWithWhiteQueen(self):
        # 1. e4 e5
        # 2. kf3 kf6
        # 3. bc4 bc5
        # 4. 0-0 0-0
        # 5. d4 d5
        # 6. d4xe5 d5xe4
        # 7. qd1xd8 rf8xd8
        # Move white pawn on E2 to E4
        self.assertTrue(self.move(E2, E4))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white knight on G1 to F3
        self.assertTrue(self.move(G1, F3))
        # Move black queen on G8 to F6
        self.assertTrue(self.move(G8, F6))
        # Move white bishop on F1 to C4
        self.assertTrue(self.move(F1, C4))
        # Move black bishop on F1 to C4
        self.assertTrue(self.move(F8, C5))
        # Castle white's king side
        self.assertTrue(self.move(E1, G1))
        # Castle black's king side
        self.assertTrue(self.move(E8, G8))
        # Move white pawn on D2 to D4
        self.assertTrue(self.move(D2, D4))
        # Move black pawn on D7 to D5
        self.assertTrue(self.move(D7, D5))
        # Capture black pawn on E5 by D4
        self.assertTrue(self.move(D4, E5))
        # Capture white pawn on E4 by D5
        self.assertTrue(self.move(D5, E4))
        # Move white queen on D1 to D8 (capture black's queen)
        self.assertTrue(self.move(D1, D8))
