import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if rook legal moves are blocked as intended
class RookCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteRookFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,A8)
        self.testUtility.movePiece(Values.rook,self.testUtility.getMove(A1,A8))
    
    def testCaptureWhiteRookFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,A1)
        self.testUtility.movePiece(Values.rook,self.testUtility.getMove(H1,A1))
    
    def testCaptureWhiteRookFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,E4)
        self.testUtility.movePieceValueToSquare(-Values.rook,F4)
        self.testUtility.validMove(\
            self.testUtility.movePiece(Values.rook,\
                self.testUtility.getMove(D4,E4)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackRookFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,A8)
        self.testUtility.movePiece(-Values.rook,self.testUtility.getMove(A1,A8))
    
    def testCaptureBlackRookFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(Values.rook,A1)
        self.testUtility.movePiece(-Values.rook,self.testUtility.getMove(H1,A1))
    
    def testCaptureBlackRookFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.rook,E4)
        self.testUtility.movePieceValueToSquare(Values.rook,F4)
        self.testUtility.validMove(\
            self.testUtility.movePiece(-Values.rook,\
                self.testUtility.getMove(D4,E4)),F4)

if __name__ == '__main__':
    unittest.main()
    