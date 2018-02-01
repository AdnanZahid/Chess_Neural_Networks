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

    def testChangeTurn(self):
        gameLogic = GameLogic()
        self.assertTrue(gameLogic.currentPlayer.color == Color.white)        
        gameLogic.changeTurn()        
        self.assertTrue(gameLogic.currentPlayer.color == Color.black)        
        gameLogic.changeTurn()        
        self.assertTrue(gameLogic.currentPlayer.color == Color.white)
    
    def testChangeBoardColor(self):
        gameLogic = GameLogic()
        self.assertTrue(gameLogic.board.currentTurnColor == Color.white)
        gameLogic.changeTurn()
        self.assertTrue(gameLogic.board.currentTurnColor == Color.black)
        gameLogic.changeTurn()
        self.assertTrue(gameLogic.board.currentTurnColor == Color.white)

if __name__ == '__main__':
    unittest.main()
    