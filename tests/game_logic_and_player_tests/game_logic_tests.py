import unittest
from tests.test_utils.test_constants import *
from src.models.board import *
from src.models.game_logic import *
from src.models.player import *
from src.models.pieces.piece_factory import *
from src.others.constants import *
from src.others.structures import *

# This class tests if game logic is working properly
class GameLogicTests(unittest.TestCase):
    
    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board

    def testMovePiece(self):
        # Move knight on B1 to C3
        piece = self.board.getPieceOnPosition(B1)
        toSquare = C3
        self.gameLogic.movePiece(EvaluationMove(piece.position,toSquare))
        self.assertTrue(piece.position == toSquare)

    def testChangeTurn(self):
        # Check current PLAYER color, should be white
        self.assertTrue(self.gameLogic.currentPlayer.color == Color.white)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current PLAYER color, should be black
        self.assertTrue(self.gameLogic.currentPlayer.color == Color.black)        
        # Change turn
        self.gameLogic.changeTurn()
        # Check current PLAYER color, should be white again
        self.assertTrue(self.gameLogic.currentPlayer.color == Color.white)
    
    def testChangeBoardColor(self):
        # Check current TURN color, should be white
        self.assertTrue(self.gameLogic.board.currentTurnColor == Color.white)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current TURN color, should be black
        self.assertTrue(self.gameLogic.board.currentTurnColor == Color.black)
        # Change turn
        self.gameLogic.changeTurn()
        # Check current TURN color, should be white again
        self.assertTrue(self.gameLogic.board.currentTurnColor == Color.white)

if __name__ == '__main__':
    unittest.main()
    