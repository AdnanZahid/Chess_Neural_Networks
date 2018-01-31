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
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteRookFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,H8)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhiteRookFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,D5)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhiteRookFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,E5)
        self.testUtility.movePieceValueToSquare(-Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.rook,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackRookFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,D4)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackRookFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,D5)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackRookFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.rook,E5)
        self.testUtility.movePieceValueToSquare(Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.rook,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    