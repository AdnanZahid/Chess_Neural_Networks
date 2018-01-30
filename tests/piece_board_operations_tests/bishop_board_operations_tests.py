import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteBishopOnD4(self):
        isPieceExists(Values.bishop,D4)
    
    def testPutWhiteBishopOnD4(self):
        movePieceValueToSquare(Values.bishop,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackBishopOnD4(self):
        isPieceExists(-Values.bishop,D4)
    
    def testPutBlackBishopOnD4(self):
        movePieceValueToSquare(-Values.bishop,D4)

if __name__ == '__main__':
    unittest.main()
    