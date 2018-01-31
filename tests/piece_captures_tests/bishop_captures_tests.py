import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopCapturesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testCaptureWhiteBishopFromA1ToH8(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,H8)
    	self.testUtility.movePiece(Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testCaptureWhiteBishopFromH1ToA8(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,A8)
    	self.testUtility.movePiece(Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testCaptureWhiteBishopFromD4ToE5ToC3(self):
    	self.testUtility.movePieceValueToSquare(-Values.bishop,E5)
    	self.testUtility.movePieceValueToSquare(-Values.bishop,C3)
    	self.testUtility.validMove(\
    		self.testUtility.movePiece(Values.bishop,\
    			self.testUtility.getMove(D4,E5)),C3)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testCaptureBlackBishopFromA1ToH8(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,H8)
    	self.testUtility.movePiece(-Values.bishop,self.testUtility.getMove(A1,H8))
    
    def testCaptureBlackBishopFromH1ToA8(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,A8)
    	self.testUtility.movePiece(-Values.bishop,self.testUtility.getMove(H1,A8))
    
    def testCaptureBlackBishopFromD4ToE5ToC3(self):
    	self.testUtility.movePieceValueToSquare(Values.bishop,E5)
    	self.testUtility.movePieceValueToSquare(Values.bishop,C3)
    	self.testUtility.validMove(\
    		self.testUtility.movePiece(-Values.bishop,\
    			self.testUtility.getMove(D4,E5)),C3)

if __name__ == '__main__':
    unittest.main()
    