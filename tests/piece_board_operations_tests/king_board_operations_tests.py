import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if king legal moves are blocked as intended
class KingBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteKingOnD4(self):
        isPieceExists(Values.king,D4)
    
    def testPutWhiteKingOnD4(self):
        movePieceValueToSquare(Values.king,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackKingOnD4(self):
        isPieceExists(-Values.king,D4)
    
    def testPutBlackKingOnD4(self):
        movePieceValueToSquare(-Values.king,D4)

if __name__ == '__main__':
    unittest.main()
    