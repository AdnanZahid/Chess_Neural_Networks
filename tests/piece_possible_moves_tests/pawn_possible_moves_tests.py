import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if pawn legal moves are blocked as intended
class PawnPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhitePawnFromA1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD5():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD4FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,C3))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD4EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,C3))
        comparisonMoves = [E5, E3, C5, C3]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackPawnFromH1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromE4():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromDE6FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.pawn,D5))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromDE6EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.pawn,D5))
        comparisonMoves = [F7, F5, D7, D5]
        self.assertEqual(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    