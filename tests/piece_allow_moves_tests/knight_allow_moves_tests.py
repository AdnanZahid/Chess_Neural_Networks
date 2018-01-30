import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if knight legal moves are allowed as intended
class KnightAllowMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testMoveWhiteKnightFromA1ToC2(self):
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(A1,C2))
    
    def testMoveWhiteKnightFromG7ToF5(self):
        self.testUtility.movePiece(Values.knight,self.testUtility.getMove(G7,F5))
    
    def testMoveWhiteKnightFromD4ToF5ToE3(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(Values.knight,self.testUtility.getMove(D4,F5)),E3)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testMoveBlackKnightFromA1ToC2(self):
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(A1,C2))
    
    def testMoveBlackKnightFromG7ToF5(self):
        self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(G7,F5))
    
    def testMoveBlackKnightFromD4ToF5ToE3(self):        
        self.testUtility.movePieceToSquare(self.testUtility.movePiece(-Values.knight,self.testUtility.getMove(D4,F5)),E3)

if __name__ == '__main__':
    unittest.main()
    