import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if king legal moves are blocked as intended
class KingBlockMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testBlockWhiteKingFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(Values.king,H8)
        self.testUtility.failToMovePiece(Values.king,self.testUtility.getMove(A1,H8))
    
    def testBlockWhiteKingFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(Values.king,D5)
        self.testUtility.failToMovePiece(Values.king,self.testUtility.getMove(H1,A8))
    
    def testBlockWhiteKingFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(Values.king,E5)
        self.testUtility.movePieceValueToSquare(Values.king,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.king,\
                self.testUtility.getMove(H1,A8)),F4)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testBlockBlackKingFromA1ToH8(self):
        self.testUtility.movePieceValueToSquare(-Values.king,D4)
        self.testUtility.failToMovePiece(-Values.king,self.testUtility.getMove(A1,H8))
    
    def testBlockBlackKingFromH1ToA8(self):
        self.testUtility.movePieceValueToSquare(-Values.king,D5)
        self.testUtility.failToMovePiece(-Values.king,self.testUtility.getMove(H1,A8))
    
    def testBlockBlackKingFromD4ToE5ToF4(self):
        self.testUtility.movePieceValueToSquare(-Values.king,E5)
        self.testUtility.movePieceValueToSquare(-Values.king,F4)
        self.testUtility.invalidMove(\
            self.testUtility.failToMovePiece(Values.king,\
                self.testUtility.getMove(D4,E5)),F4)

if __name__ == '__main__':
    unittest.main()
    