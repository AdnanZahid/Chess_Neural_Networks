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

    # ///////////
    # // WHITE //
    # ///////////
    
    def testPossibleMovesWhitePawnFromA1(self):
        piece = self.testUtility.movePieceValueToSquare(Values.pawn,A2)

        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [A3, A4]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD5(self):
        piece = self.testUtility.movePieceValueToSquare(Values.pawn,D5)
        piece.hasMoved = True

        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [D6]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD4FriendlyFire(self):
        piece = self.testUtility.movePieceValueToSquare(Values.pawn,D4)

        self.testUtility.movePieceValueToSquare(Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(Values.pawn,D5)
        self.testUtility.movePieceValueToSquare(Values.pawn,C5)
        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesWhitePawnFromD4EnemyFire(self):
        piece = self.testUtility.movePieceValueToSquare(Values.pawn,D4)

        self.testUtility.movePieceValueToSquare(-Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,D5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,C5)
        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [E5, C5]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    # ///////////
    # // BLACK //
    # ///////////
    
    def testPossibleMovesBlackPawnFromH7(self):
        piece = self.testUtility.movePieceValueToSquare(-Values.pawn,H7)

        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [H6, H5]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromE4(self):
        piece = self.testUtility.movePieceValueToSquare(-Values.pawn,E4)
        piece.hasMoved = True

        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [E3]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromDE6FriendlyFire(self):
        piece = self.testUtility.movePieceValueToSquare(-Values.pawn,E6)

        self.testUtility.movePieceValueToSquare(-Values.pawn,F5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(-Values.pawn,D5)
        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = []
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)
    
    def testPossibleMovesBlackPawnFromDE6EnemyFire(self):
        piece = self.testUtility.movePieceValueToSquare(-Values.pawn,E6)

        self.testUtility.movePieceValueToSquare(Values.pawn,F5)
        self.testUtility.movePieceValueToSquare(Values.pawn,E5)
        self.testUtility.movePieceValueToSquare(Values.pawn,D5)
        possibleMoves = self.testUtility.generateAllMoves(piece)
        comparisonMoves = [F5, D5]
        self.testUtility.checkEqualMoves(possibleMoves,comparisonMoves)

if __name__ == '__main__':
    unittest.main()
    