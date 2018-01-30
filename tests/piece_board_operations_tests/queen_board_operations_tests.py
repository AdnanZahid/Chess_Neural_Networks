import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if queen legal moves are blocked as intended
class QueenBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhiteQueenOnD4(self):
        isPieceExists(Values.queen,D4)
    
    def testPutWhiteQueenOnD4(self):
        movePieceValueToSquare(Values.queen,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackQueenOnD4(self):
        isPieceExists(-Values.queen,D4)
    
    def testPutBlackQueenOnD4(self):
        movePieceValueToSquare(-Values.queen,D4)

if __name__ == '__main__':
    unittest.main()
    