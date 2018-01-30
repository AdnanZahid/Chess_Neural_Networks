import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if rook legal moves are blocked as intended
class RookBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteRookOnD4(self):
        isPieceExists(Values.rook,D4)
    
    def testPutWhiteRookOnD4(self):
        movePieceValueToSquare(Values.rook,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackRookOnD4(self):
        isPieceExists(-Values.rook,D4)
    
    def testPutBlackRookOnD4(self):
        movePieceValueToSquare(-Values.rook,D4)

if __name__ == '__main__':
    unittest.main()
    