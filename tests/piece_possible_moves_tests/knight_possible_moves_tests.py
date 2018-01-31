import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if knight legal moves are blocked as intended
class KnightPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteKnightFromA1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD5():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD4FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,C3))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD4EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,C3))
        comparisonMoves = [E5, E3, C5, C3]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackKnightFromH1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromE4():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromDE6FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D5))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromDE6EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,D5))
        comparisonMoves = [F7, F5, D7, D5]
        self.assertEqual(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    