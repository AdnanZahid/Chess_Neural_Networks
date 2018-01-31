import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if queen legal moves are blocked as intended
class QueenBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,H8)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(A1,H8))
    
    def testBlockWhiteQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D5)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(H1,A8))
    
    def testBlockWhiteQueenFromD4ToE5ToF6(self):
        self.testUtility.movePieceValueToSquare(Values.queen,E5)
        self.testUtility.movePieceValueToSquare(Values.queen,F6)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(D4,E5)),F6)
    
    def testBlockWhiteQueenFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.queen,A8)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(A1,A8))
    
    def testBlockWhiteQueenFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(Values.queen,A1)
        self.testUtility.failToMovePiece(Values.queen,self.testUtility.getMove(H1,A1))
    
    def testBlockWhiteQueenFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.queen,E4)
        self.testUtility.movePieceValueToSquare(Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.queen,\
                self.testUtility.getMove(D4,E4)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackQueenFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D4)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackQueenFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D5)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackQueenFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,E5)
        self.testUtility.movePieceValueToSquare(-Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(-Values.queen,\
                self.testUtility.getMove(D4,E5)),F4)
    
    def testBlockBlackQueenFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,A8)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(A1,A8))
    
    def testBlockBlackQueenFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,A1)
        self.testUtility.failToMovePiece(-Values.queen,self.testUtility.getMove(H1,A1))
    
    def testBlockBlackQueenFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,E4)
        self.testUtility.movePieceValueToSquare(-Values.queen,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(-Values.queen,\
                self.testUtility.getMove(D4,E4)),F4)

if __name__ == '__main__':
    unittest.main()
    