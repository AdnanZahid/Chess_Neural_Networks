import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if pawn legal moves are allowed as intended
class PawnAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhitePawnFromA2ToA4(self):
        self.testUtility.movePiece(Values.pawn,self.testUtility.getMove(A2,A4))
    
    def testMoveWhitePawnFromF6ToF7(self):
        self.testUtility.movePiece(Values.pawn,self.testUtility.getMove(F6,F7))
    
    def testMoveWhitePawnFromD2ToD3ToD4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.pawn,self.testUtility.getMove(D2,D3)),D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackPawnFromA7ToA5(self):
        self.testUtility.movePiece(-Values.pawn,self.testUtility.getMove(A7,A5))
    
    def testMoveBlackPawnFromF7ToF6(self):
        self.testUtility.movePiece(-Values.pawn,self.testUtility.getMove(F7,F6))
    
    def testMoveBlackPawnFromD7ToD6ToD5(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.pawn,self.testUtility.getMove(D7,D6)),D5)

if __name__ == '__main__':
    unittest.main()
    