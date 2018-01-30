import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if rook legal moves are blocked as intended
class RookBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteRookFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,H8)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(A1,H8))
    
    def testBlockWhiteRookFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.rook,D5)
        self.testUtility.failToMovePiece(Values.rook,self.testUtility.getMove(H1,A8))
    
    def testBlockWhiteRookFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.rook,E5)
        self.testUtility.movePieceValueToSquare(Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.rook,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackRookFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,D4)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackRookFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,D5)
        self.testUtility.failToMovePiece(-Values.rook,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackRookFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.rook,E5)
        self.testUtility.movePieceValueToSquare(-Values.rook,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.rook,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    