import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if queen legal moves are blocked as intended
class QueenPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteQueenFromA1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteQueenFromD5():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteQueenFromD4FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,C3))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteQueenFromD4EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,C3))
        comparisonMoves = [E5, E3, C5, C3]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackQueenFromH1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackQueenFromE4():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackQueenFromDE6FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.queen,D5))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackQueenFromDE6EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.queen,D5))
        comparisonMoves = [F7, F5, D7, D5]
        self.assertEqual(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    