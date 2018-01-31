import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if queen legal moves are blocked as intended
class QueenCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,H8)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhiteQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D5)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhiteQueenFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,E5)
        self.testUtility.movePieceValueToSquare(-Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(H1,A8)),F4)
    
    def testCaptureWhiteQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,H8)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhiteQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D5)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhiteQueenFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,E5)
        self.testUtility.movePieceValueToSquare(-Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D4)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D5)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackQueenFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.queen,E5)
        self.testUtility.movePieceValueToSquare(Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(D4,E5)),F4)
    
    def testCaptureBlackQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D4)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D5)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackQueenFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.queen,E5)
        self.testUtility.movePieceValueToSquare(Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    