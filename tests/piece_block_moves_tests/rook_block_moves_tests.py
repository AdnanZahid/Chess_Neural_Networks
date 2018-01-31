import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if rook legal moves are blocked as intended
class RookBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteRookFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,A8)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(A1,A8))
    
    def testBlockWhiteRookFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(Values.rook,A1)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(H1,A1))
    
    def testBlockWhiteRookFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.rook,E4)
        self.testUtility.movePieceValueToSquare(Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.rook,\
                self.testUtility.getMove(D4,E4)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackRookFromA1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,A8)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(A1,A8))
    
    def testBlockBlackRookFromH1ToA1(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,A1)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(H1,A1))
    
    def testBlockBlackRookFromD4ToE4ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,E4)
        self.testUtility.movePieceValueToSquare(-Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(-Values.rook,\
                self.testUtility.getMove(D4,E4)),F4)

if __name__ == '__main__':
    unittest.main()
    