import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if queen legal moves are blocked as intended
class QueenBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteQueenOnD4(self):
        self.testUtility.isPieceExists(Values.queen,D4)
    
    def testPutWhiteQueenOnD4(self):
        self.testUtility.movePieceValueToSquare(Values.queen,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackQueenOnD4(self):
        self.testUtility.isPieceExists(-Values.queen,D4)
    
    def testPutBlackQueenOnD4(self):
        self.testUtility.movePieceValueToSquare(-Values.queen,D4)

if __name__ == '__main__':
    unittest.main()
    