from src.models.board import *
from src.models.player import *
from src.others.structures import *


# This class represents all the game logic in general
class GameLogic:

    def __init__(self):
        self.board = Board()
        self.whitePlayer = Player(Color.white, self.board)
        self.blackPlayer = Player(Color.black, self.board)

        self.whitePlayer.opponent = self.blackPlayer
        self.blackPlayer.opponent = self.whitePlayer

        self.currentPlayer = self.whitePlayer

    def move(self, move):
        if self.currentPlayer.move(move):
            self.changeTurn()
            return True
        return False

    def changeTurn(self):
        self.currentPlayer = self.currentPlayer.opponent

    def isAITurn(self):
        return False
