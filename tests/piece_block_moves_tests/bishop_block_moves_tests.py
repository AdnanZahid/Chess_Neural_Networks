import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteBishopFromA1ToH8(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,H8)
    	self.testUtility.failToMovePiece(Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testBlockWhiteBishopFromH1ToA8(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,D5)
    	self.testUtility.failToMovePiece(Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testBlockWhiteBishopFromD4ToE5ToC3(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,E5)
    	self.testUtility.movePieceValueToSquare(Values.bishop,C3)
    	self.testUtility.invalidMove(\
    		self.testUtility.failToMovePiece(Values.bishop,\
    			self.testUtility.getMove(D4,E5)),C3)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackBishopFromA1ToH8(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,D4)
    	self.testUtility.failToMovePiece(-Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackBishopFromH1ToA8(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,D5)
    	self.testUtility.failToMovePiece(-Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackBishopFromD4ToE5ToC3(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,E5)
    	self.testUtility.movePieceValueToSquare(-Values.bishop,C3)
    	self.testUtility.invalidMove(\
    		self.testUtility.failToMovePiece(-Values.bishop,\
    			self.testUtility.getMove(D4,E5)),C3)

if __name__ == '__main__':
    unittest.main()
    