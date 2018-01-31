import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if pawn legal moves are blocked as intended
class PawnCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhitePawnFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,H8)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhitePawnFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,D5)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhitePawnFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.pawn,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackPawnFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,D4)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackPawnFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,D5)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackPawnFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(Values.pawn,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.pawn,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    