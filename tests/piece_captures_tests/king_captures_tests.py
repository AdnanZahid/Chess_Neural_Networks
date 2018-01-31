import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if king legal moves are blocked as intended
class KingCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteKingFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.king,H8)
        self.testUtility.failToMovePiece(Values.king,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhiteKingFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.king,D5)
        self.testUtility.failToMovePiece(Values.king,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhiteKingFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.king,E5)
        self.testUtility.movePieceValueToSquare(-Values.king,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.king,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackKingFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.king,D4)
        self.testUtility.failToMovePiece(-Values.king,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackKingFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.king,D5)
        self.testUtility.failToMovePiece(-Values.king,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackKingFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.king,E5)
        self.testUtility.movePieceValueToSquare(Values.king,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.king,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    