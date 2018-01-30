import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if pawn legal moves are blocked as intended
class PawnBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhitePawnFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,H8)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(A1,H8))
    
    def testBlockWhitePawnFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,D5)
        self.testUtility.failToMovePiece(Values.pawn,self.testUtility.getMove(H1,A8))
    
    def testBlockWhitePawnFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(Values.pawn,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.pawn,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackPawnFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,D4)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackPawnFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,D5)
        self.testUtility.failToMovePiece(-Values.pawn,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackPawnFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.pawn,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    