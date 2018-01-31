import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if king legal moves are blocked as intended
class KingBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteKingOnD4(self):
        self.testUtility.isPieceExists(Values.king,D4)
    
    def testPutWhiteKingOnD4(self):
        self.testUtility.movePieceValueToSquare(Values.king,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackKingOnD4(self):
        self.testUtility.isPieceExists(-Values.king,D4)
    
    def testPutBlackKingOnD4(self):
        self.testUtility.movePieceValueToSquare(-Values.king,D4)

if __name__ == '__main__':
    unittest.main()
    