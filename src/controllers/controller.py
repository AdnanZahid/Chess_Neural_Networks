from src.controllers.input_output_handlers import *
from src.models.game_logic import *
from src.views.view import *


# This class handles controller logic
class Controller(InputHandlerDelegate):

    def __init__(self):
        self.setupNewGame()

    def setupNewGame(self):
        # Set game over to false by default
        self.gameOver = False
        # SET GAMELOGIC with AI or HUMAN PLAYERS
        self.gameLogic = GameLogic(isWhitePlayerAI=False, isBlackPlayerAI=False)
        # SET VIEW as OUTPUTHANDLER
        self.view = View()
        self.outputHandler = self.view
        # CHOSE whether to RUN CHESS ENGINE on MAIN QUEUE OR A SEPARATE ONE
        self.runEngine()

    # RUN CHESS ENGINE
    def runEngine(self):
        while not (self.gameOver):
            # CHECK if it is AI TURN
            if self.gameLogic.isAITurn():
                # ASSIGN GAMELOGIC to INPUTHANDLER - FOR AI MOVES
                self.inputHandler = self.gameLogic
            # ELSE it is HUMAN TURN
            else:
                # ASSIGN OUTPUTHANDLER (VIEW) to INPUTHANDLER - FOR HUMAN MOVES
                self.inputHandler = self.outputHandler
            # SET SELF as VIEW DELEGATE
            self.inputHandler.inputHandlerDelegate = self
            # TAKE INPUT from INPUTHANDLER
            self.inputHandler.input(self.gameLogic)
        self.setupNewGame()

    # PlAY HUMAN MOVE
    def didTakeInput(self, move):
        # TELL GAMELOGIC to MAKE the MOVE if VALID
        if self.gameLogic.move(move):
            # SHOW OUTPUT on VIEW
            self.outputHandler.output()
            if self.gameLogic.currentPlayer.isUnderCheckMate(self.gameLogic.board):
                self.gameOver = True
        else:
            # CANCEL MOVE on VIEW (PUT PIECE DOWN)
            self.outputHandler.cancelMove()
