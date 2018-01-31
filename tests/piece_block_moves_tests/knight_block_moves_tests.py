import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are blocked as intended
class KnightBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteKnightFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.knight,H8)
        self.testUtility.failToMovePiece(Values.knight,self.testUtility.getMove(A1,H8))
    
    def testBlockWhiteKnightFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.knight,D5)
        self.testUtility.failToMovePiece(Values.knight,self.testUtility.getMove(H1,A8))
    
    def testBlockWhiteKnightFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.knight,E5)
        self.testUtility.movePieceValueToSquare(Values.knight,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.knight,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackKnightFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,D4)
        self.testUtility.failToMovePiece(-Values.knight,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackKnightFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,D5)
        self.testUtility.failToMovePiece(-Values.knight,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackKnightFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,E5)
        self.testUtility.movePieceValueToSquare(-Values.knight,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.knight,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    