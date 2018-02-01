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

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteKnightFromA1(self):
        self.board.currentTurnColor = Color.white
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,A1))
        comparisonMoves = [B3, C2]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD5(self):
        self.board.currentTurnColor = Color.white
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D5))
        comparisonMoves = [E7, F6, C7, B6, E3, F4, C3, B4]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD4FriendlyFire(self):
        self.board.currentTurnColor = Color.white
        self.testUtility.movePieceValueToSquare(Values.knight,E6)
        self.testUtility.movePieceValueToSquare(Values.knight,E2)
        self.testUtility.movePieceValueToSquare(Values.knight,F5)
        self.testUtility.movePieceValueToSquare(Values.knight,F3)
        self.testUtility.movePieceValueToSquare(Values.knight,C6)
        self.testUtility.movePieceValueToSquare(Values.knight,C2)
        self.testUtility.movePieceValueToSquare(Values.knight,B5)
        self.testUtility.movePieceValueToSquare(Values.knight,B3)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteKnightFromD4EnemyFire(self):
        self.board.currentTurnColor = Color.white
        self.testUtility.movePieceValueToSquare(-Values.knight,E6)
        self.testUtility.movePieceValueToSquare(-Values.knight,E2)
        self.testUtility.movePieceValueToSquare(-Values.knight,F5)
        self.testUtility.movePieceValueToSquare(-Values.knight,F3)
        self.testUtility.movePieceValueToSquare(-Values.knight,C6)
        self.testUtility.movePieceValueToSquare(-Values.knight,C2)
        self.testUtility.movePieceValueToSquare(-Values.knight,B5)
        self.testUtility.movePieceValueToSquare(-Values.knight,B3)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.knight,D4))
        comparisonMoves = [E6, E2, F5, F3, C6, C2, B5, B3]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackKnightFromH1(self):
        self.board.currentTurnColor = Color.black
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,H1))
        comparisonMoves = [G3, F2]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromE4(self):
        self.board.currentTurnColor = Color.black
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E4))
        comparisonMoves = [F6, G5, D6, C5, F2, G3, D2, C3]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromDE6FriendlyFire(self):
        self.board.currentTurnColor = Color.black
        self.testUtility.movePieceValueToSquare(-Values.knight,F8)
        self.testUtility.movePieceValueToSquare(-Values.knight,F4)
        self.testUtility.movePieceValueToSquare(-Values.knight,G7)
        self.testUtility.movePieceValueToSquare(-Values.knight,G5)
        self.testUtility.movePieceValueToSquare(-Values.knight,D8)
        self.testUtility.movePieceValueToSquare(-Values.knight,D4)
        self.testUtility.movePieceValueToSquare(-Values.knight,C7)
        self.testUtility.movePieceValueToSquare(-Values.knight,C5)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackKnightFromDE6EnemyFire(self):
        self.board.currentTurnColor = Color.black
        self.testUtility.movePieceValueToSquare(Values.knight,F8)
        self.testUtility.movePieceValueToSquare(Values.knight,F4)
        self.testUtility.movePieceValueToSquare(Values.knight,G7)
        self.testUtility.movePieceValueToSquare(Values.knight,G5)
        self.testUtility.movePieceValueToSquare(Values.knight,D8)
        self.testUtility.movePieceValueToSquare(Values.knight,D4)
        self.testUtility.movePieceValueToSquare(Values.knight,C7)
        self.testUtility.movePieceValueToSquare(Values.knight,C5)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.knight,E6))
        comparisonMoves = [F8, F4, G7, G5, D8, D4, C7, C5]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    