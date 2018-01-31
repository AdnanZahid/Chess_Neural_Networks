import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if king legal moves are allowed as intended
class KingAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteKingFromA1ToB2(self):
        self.testUtility.movePiece(Values.king,self.testUtility.getMove(A1,B2))
    
    def testMoveWhiteKingFromG7ToG8(self):
        self.testUtility.movePiece(Values.king,self.testUtility.getMove(G7,G8))
    
    def testMoveWhiteKingFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.king,self.testUtility.getMove(D4,E5)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackKingFromA1ToB2(self):
        self.testUtility.movePiece(-Values.king,self.testUtility.getMove(A1,B2))
    
    def testMoveBlackKingFromG7ToG8(self):
        self.testUtility.movePiece(-Values.king,self.testUtility.getMove(G7,G8))
    
    def testMoveBlackKingFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.king,self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    