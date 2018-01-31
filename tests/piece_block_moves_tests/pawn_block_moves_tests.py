import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if pawn legal moves are blocked as intended
class PawnBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhitePawnFromA2ToA4(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,A4)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(A2,A4))
    
    def testBlockWhitePawnFromH6ToH7(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,H7)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(H6,H7))
    
    def testBlockWhitePawnFromD2ToD3ToD4(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,D3)
        self.testUtility.movePieceValueToSquare(Values.pawn,D4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.pawn,\
                self.testUtility.getMove(D2,D3)),D4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackPawnFromA7ToA5(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,A5)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(A7,A5))
    
    def testBlockBlackPawnFromH5ToH4(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,H4)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(H5,H4))
    
    def testBlockBlackPawnFromE7ToE6ToE5(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,E6)
        self.testUtility.movePieceValueToSquare(-Values.pawn,E5)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(-Values.pawn,\
                self.testUtility.getMove(E7,E6)),E5)

if __name__ == '__main__':
    unittest.main()
    