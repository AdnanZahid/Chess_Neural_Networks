import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are blocked as intended
class KnightCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteKnightFromA1ToC2(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,C2)
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(A1,C2))
    
    def testCaptureWhiteKnightFromH1ToG3(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,G3)
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(H1,G3))
    
    def testCaptureWhiteKnightFromD6ToE6ToF2(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,E4)
        self.testUtility.movePieceValueToSquare(-Values.knight,F2)
        self.testUtility.validMove(\
            self.testUtility.movePiece(Values.knight,\
                self.testUtility.getMove(D6,E4)),F2)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackKnightFromA1ToC2(self):
        self.testUtility.movePieceValueToSquare(Values.knight,C2)
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(A1,C2))
    
    def testCaptureBlackKnightFromH1ToG3(self):
        self.testUtility.movePieceValueToSquare(Values.knight,G3)
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(H1,G3))
    
    def testCaptureBlackKnightFromD4ToE6ToF8(self):
        self.testUtility.movePieceValueToSquare(Values.knight,E6)
        self.testUtility.movePieceValueToSquare(Values.knight,F8)
        self.testUtility.validMove(\
            self.testUtility.movePiece(-Values.knight,\
                self.testUtility.getMove(D4,E6)),F8)

if __name__ == '__main__':
    unittest.main()
    