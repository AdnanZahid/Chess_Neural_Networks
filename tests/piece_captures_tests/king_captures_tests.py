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

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteKingFromG7ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,H8)
        self.testUtility.movePiece(Values.king,self.testUtility.getMove(G7,H8))
    
    def testCaptureWhiteKingFromD4ToD5(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D5)
        self.testUtility.movePiece(Values.king,self.testUtility.getMove(D4,D5))
    
    def testCaptureWhiteKingFromD6ToE5ToD5(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,E5)
        self.testUtility.movePieceValueToSquare(-Values.queen,D5)
        self.testUtility.validMove(\
            self.testUtility.movePiece(Values.king,\
                self.testUtility.getMove(D6,E5)),D5)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackKingFromC4ToD4(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D4)
        self.testUtility.movePiece(-Values.king,self.testUtility.getMove(C4,D4))
    
    def testCaptureBlackKingFromA3ToA2(self):
        self.testUtility.movePieceValueToSquare(Values.queen,A2)
        self.testUtility.movePiece(-Values.king,self.testUtility.getMove(A3,A2))
    
    def testCaptureBlackKingFromD4ToE5ToD5(self):
        self.testUtility.movePieceValueToSquare(Values.queen,E5)
        self.testUtility.movePieceValueToSquare(Values.queen,D5)
        self.testUtility.validMove(\
            self.testUtility.movePiece(-Values.king,\
                self.testUtility.getMove(D4,E5)),D5)

if __name__ == '__main__':
    unittest.main()
    