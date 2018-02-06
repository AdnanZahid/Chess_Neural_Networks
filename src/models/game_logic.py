from src.models.board import *
from src.models.player import *
from src.models.pieces.piece_factory import *
from src.others.structures import *

# This class represents all the game logic in general
class GameLogic:
    
    def __init__(self):
        self.board = Board()
        self.whitePlayer = Player(Color.white,self.board)
        self.blackPlayer = Player(Color.black,self.board)
        
        self.whitePlayer.opponent = self.blackPlayer
        self.blackPlayer.opponent = self.whitePlayer
        
        self.currentPlayer = self.whitePlayer
    
    def movePiece(self,move):
        result = False
        
        if self.currentPlayer.movePiece(move,True):
            self.changeTurn()
            result = True
        
        return result
    
    def changeTurn(self):        
        self.currentPlayer = self.currentPlayer.opponent
        self.board.currentTurnColor = self.currentPlayer.color
    
    def isAITurn(self):            
        return False
        
    def input(self):
        inputHandlerDelegate.didTakeInput(currentPlayer.generateMove())
