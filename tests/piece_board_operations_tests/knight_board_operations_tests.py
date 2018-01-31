import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are blocked as intended
class KnightBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteKnightOnD4(self):
        isPieceExists(Values.knight,D4)
    
    def testPutWhiteKnightOnD4(self):
        movePieceValueToSquare(Values.knight,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackKnightOnD4(self):
        isPieceExists(-Values.knight,D4)
    
    def testPutBlackKnightOnD4(self):
        movePieceValueToSquare(-Values.knight,D4)

if __name__ == '__main__':
    unittest.main()
    