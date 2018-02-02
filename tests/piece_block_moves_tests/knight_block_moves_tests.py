import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are blocked as intended
class KnightBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteKnightFromA1ToC2(self):
        self.testUtility.movePieceValueToSquare(Values.knight,C2)
        self.testUtility.failToMovePiece(Values.knight,self.testUtility.getMove(A1,C2))
    
    def testBlockWhiteKnightFromH1ToG3(self):
        self.testUtility.movePieceValueToSquare(Values.knight,G3)
        self.testUtility.failToMovePiece(Values.knight,self.testUtility.getMove(H1,G3))
    
    def testBlockWhiteKnightFromD6ToE6ToF5(self):
        self.testUtility.movePieceValueToSquare(Values.knight,E4)
        self.testUtility.movePieceValueToSquare(Values.knight,F6)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.knight,\
                self.testUtility.getMove(D6,E4)),F6)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackKnightFromA1ToC2(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,C2)
        self.testUtility.failToMovePiece(-Values.knight,self.testUtility.getMove(A1,C2))
    
    def testBlockBlackKnightFromH1ToG3(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,G3)
        self.testUtility.failToMovePiece(-Values.knight,self.testUtility.getMove(H1,G3))
    
    def testBlockBlackKnightFromD4ToE6ToF5(self):
        self.testUtility.movePieceValueToSquare(-Values.knight,E6)
        self.testUtility.movePieceValueToSquare(-Values.knight,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(-Values.knight,\
                self.testUtility.getMove(D4,E6)),F4)

if __name__ == '__main__':
    unittest.main()
    