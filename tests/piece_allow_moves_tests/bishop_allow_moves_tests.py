import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if bishop legal moves are allowed as intended
class BishopAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteBishopFromA1ToH8(self):
        self.testUtility.movePiece(Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testMoveWhiteBishopFromH1ToA8(self):
        self.testUtility.movePiece(Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testMoveWhiteBishopFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.bishop,self.testUtility.getMove(D4,E5)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackBishopFromA1ToH8(self):
        self.testUtility.movePiece(-Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testMoveBlackBishopFromH1ToA8(self):
        self.testUtility.movePiece(-Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testMoveBlackBishopFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.bishop,self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    