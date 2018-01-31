import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are allowed as intended
class KnightAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteKnightFromA1ToC2(self):
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(A1,C2))
    
    def testMoveWhiteKnightFromG7ToF5(self):
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(G7,F5))
    
    def testMoveWhiteKnightFromD4ToF5ToE3(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.knight,self.testUtility.getMove(D4,F5)),E3)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackKnightFromA1ToC2(self):
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(A1,C2))
    
    def testMoveBlackKnightFromG7ToF5(self):
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(G7,F5))
    
    def testMoveBlackKnightFromD4ToF5ToE3(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(D4,F5)),E3)

if __name__ == '__main__':
    unittest.main()
    