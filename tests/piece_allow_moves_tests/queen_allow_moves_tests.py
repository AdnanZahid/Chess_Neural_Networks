import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if queen legal moves are allowed as intended
class QueenAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteQueenFromA1ToH8(self):
        self.testUtility.movePiece(Values.queen,self.testUtility.getMove(A1,H8))
    
    def testMoveWhiteQueenFromH1ToA8(self):
        self.testUtility.movePiece(Values.queen,self.testUtility.getMove(H1,A8))
    
    def testMoveWhiteQueenFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.queen,self.testUtility.getMove(D4,E5)),F4)
        
    def testMoveWhiteQueenFromA1ToA8(self):
        self.testUtility.movePiece(Values.queen,self.testUtility.getMove(A1,A8))
    
    def testMoveWhiteQueenFromH8ToA8(self):
        self.testUtility.movePiece(Values.queen,self.testUtility.getMove(H8,A8))
    
    def testMoveWhiteQueenFromD4ToD5ToF5(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.queen,self.testUtility.getMove(D4,D5)),F5)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackQueenFromA1ToH8(self):
        self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(A1,H8))
    
    def testMoveBlackQueenFromH1ToA8(self):
        self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(H1,A8))
    
    def testMoveBlackQueenFromD4ToE5ToF4(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(D4,E5)),F4)
    
    def testMoveBlackQueenFromA1ToA8(self):
        self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(A1,A8))
    
    def testMoveBlackQueenFromH8ToA8(self):
        self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(H8,A8))
    
    def testMoveBlackQueenFromD4ToD5ToF5(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.queen,self.testUtility.getMove(D4,D5)),F5)

if __name__ == '__main__':
    unittest.main()
    