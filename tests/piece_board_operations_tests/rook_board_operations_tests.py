import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if rook legal moves are blocked as intended
class RookBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteRookOnD4(self):
        self.testUtility.isPieceExists(Values.rook,D4)
    
    def testPutWhiteRookOnD4(self):
        self.testUtility.movePieceValueToSquare(Values.rook,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackRookOnD4(self):
        self.testUtility.isPieceExists(-Values.rook,D4)
    
    def testPutBlackRookOnD4(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,D4)

if __name__ == '__main__':
    unittest.main()
    