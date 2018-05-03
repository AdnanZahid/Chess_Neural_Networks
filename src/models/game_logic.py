from src.models.ai_player import *
from src.models.board import *
from src.others.fen_helper import *
from src.others.pgn_helper import *


# This class represents all the game logic in general
class GameLogic:

    def __init__(self, isWhitePlayerAI=False, isBlackPlayerAI=False):
        self.board = Board()

        if isWhitePlayerAI:
            self.whitePlayer = AIPlayer(Color.white, self.board)
        else:
            self.whitePlayer = Player(Color.white, self.board)

        if isBlackPlayerAI:
            self.blackPlayer = AIPlayer(Color.black, self.board)
        else:
            self.blackPlayer = Player(Color.black, self.board)

        self.whitePlayer.opponent = self.blackPlayer
        self.blackPlayer.opponent = self.whitePlayer

        self.currentPlayer = self.whitePlayer

        self.fen_helper = FENHelper(self)
        self.pgn_helper = PGNHelper(self)

    def move(self, move):
        if self.currentPlayer.move(move):
            self.changeTurn()
            return True
        return False

    def changeTurn(self):
        self.currentPlayer = self.currentPlayer.opponent

    def isAITurn(self):
        return self.currentPlayer.isAI

    def input(self):
        self.inputHandlerDelegate.didTakeInput(self.currentPlayer.generateMove())
