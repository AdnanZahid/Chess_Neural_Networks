import unittest
from TestUtility import *
from TestConstants import *
from Board import *
from Constants import *
from Structures import *

# This class tests if rook legal moves are blocked as intended
class RookPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteRookFromA1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteRookFromD5():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteRookFromD4FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,C3))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteRookFromD4EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,E5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,E3))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,C5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,C3))
        comparisonMoves = [E5, E3, C5, C3]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackRookFromH1():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackRookFromE4():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackRookFromDE6FriendlyFire():
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.rook,D5))
        comparisonMoves = []
        self.assertEqual(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackRookFromDE6EnemyFire():
        
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,F7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,F5))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,D7))
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.rook,D5))
        comparisonMoves = [F7, F5, D7, D5]
        self.assertEqual(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    