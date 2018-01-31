import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteBishopOnD4(self):
        self.testUtility.isPieceExists(Values.bishop,D4)
    
    def testPutWhiteBishopOnD4(self):
        self.testUtility.movePieceValueToSquare(Values.bishop,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackBishopOnD4(self):
        self.testUtility.isPieceExists(-Values.bishop,D4)
    
    def testPutBlackBishopOnD4(self):
        self.testUtility.movePieceValueToSquare(-Values.bishop,D4)

if __name__ == '__main__':
    unittest.main()
    