import unittest
from tests.test_utils.test_utility import *
from tests.test_utils.test_constants import *
from src.models.board import *
from src.others.constants import *
from src.others.structures import *

# This class tests if bishop legal moves are blocked as intended
class BishopPossibleMovesTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.testUtility = TestUtility(self.board)

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhiteBishopFromA1(self):
        self.board.currentTurnColor = Color.white
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,A1))
        comparisonMoves = [B2, C3, D4, E5, F6, G7, H8]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD5(self):
        self.board.currentTurnColor = Color.white
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D5))
        comparisonMoves = [E6, F7, G8, E4, F3, G2, H1, C6, B7, A8, C4, B3, A2]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD4FriendlyFire(self):
        self.board.currentTurnColor = Color.white
        self.testUtility.movePieceValueToSquare(Values.bishop,E5)
        self.testUtility.movePieceValueToSquare(Values.bishop,E3)
        self.testUtility.movePieceValueToSquare(Values.bishop,C5)
        self.testUtility.movePieceValueToSquare(Values.bishop,C3)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D4))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhiteBishopFromD4EnemyFire(self):
        self.board.currentTurnColor = Color.white
        self.testUtility.movePieceValueToSquare(-Values.bishop,E5)
        self.testUtility.movePieceValueToSquare(-Values.bishop,E3)
        self.testUtility.movePieceValueToSquare(-Values.bishop,C5)
        self.testUtility.movePieceValueToSquare(-Values.bishop,C3)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(Values.bishop,D4))
        comparisonMoves = [E5, E3, C5, C3]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackBishopFromH1(self):
        self.board.currentTurnColor = Color.black
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,H1))
        comparisonMoves = [G2, F3, E4, D5, C6, B7, A8]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromE4(self):
        self.board.currentTurnColor = Color.black
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E4))
        comparisonMoves = [F5, G6, H7, F3, G2, H1, D5, C6, B7, A8, D3, C2, B1]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromDE6FriendlyFire(self):
        self.board.currentTurnColor = Color.black
        self.testUtility.movePieceValueToSquare(-Values.bishop,F7)
        self.testUtility.movePieceValueToSquare(-Values.bishop,F5)
        self.testUtility.movePieceValueToSquare(-Values.bishop,D7)
        self.testUtility.movePieceValueToSquare(-Values.bishop,D5)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E6))
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackBishopFromDE6EnemyFire(self):
        self.board.currentTurnColor = Color.black
        self.testUtility.movePieceValueToSquare(Values.bishop,F7)
        self.testUtility.movePieceValueToSquare(Values.bishop,F5)
        self.testUtility.movePieceValueToSquare(Values.bishop,D7)
        self.testUtility.movePieceValueToSquare(Values.bishop,D5)
        possibleMoves = self.testUtility.generateAllMoves(self.testUtility.movePieceValueToSquare(-Values.bishop,E6))
        comparisonMoves = [F7, F5, D7, D5]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    