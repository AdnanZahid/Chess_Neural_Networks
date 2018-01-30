import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if pawn legal moves are blocked as intended
class PawnBoardOperationsTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testGetWhitePawnOnD4(self):
        isPieceExists(Values.pawn,D4)
    
    def testPutWhitePawnOnD4(self):
        movePieceValueToSquare(Values.pawn,D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testGetBlackPawnOnD4(self):
        isPieceExists(-Values.pawn,D4)
    
    def testPutBlackPawnOnD4(self):
        movePieceValueToSquare(-Values.pawn,D4)

if __name__ == '__main__':
    unittest.main()
    