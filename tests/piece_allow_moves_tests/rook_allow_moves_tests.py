import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if rook legal moves are allowed as intended
class RookAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteRookFromA1ToA8(self):
        self.testUtility.movePiece(Values.rook,self.testUtility.getMove(A1,A8))
    
    def testMoveWhiteRookFromH8ToA8(self):
        self.testUtility.movePiece(Values.rook,self.testUtility.getMove(H8,A8))
    
    def testMoveWhiteRookFromD4ToD5ToF5(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.rook,self.testUtility.getMove(D4,D5)),F5)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackRookFromA1ToA8(self):
        self.testUtility.movePiece(-Values.rook,self.testUtility.getMove(A1,A8))
    
    def testMoveBlackRookFromH8ToA8(self):
        self.testUtility.movePiece(-Values.rook,self.testUtility.getMove(H8,A8))
    
    def testMoveBlackRookFromD4ToD5ToF5(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.rook,self.testUtility.getMove(D4,D5)),F5)

if __name__ == '__main__':
    unittest.main()
    