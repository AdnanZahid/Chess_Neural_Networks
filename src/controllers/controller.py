from src.models.game_logic import *
from src.controllers.input_output_handlers import *
from src.views.view import *

# This class handles controller logic
class Controller(InputHandlerDelegate):
    
    def __init__(self):
        
        # SET GAMELOGIC with AI or HUMAN PLAYERS
        self.gameLogic = GameLogic()
        
        # SET VIEW as OUTPUTHANDLER
        view = View()
        self.outputHandler = view
        
        # CHOSE whether to RUN CHESS ENGINE on MAIN QUEUE OR A SEPARATE ONE
        self.runEngine(view)
    
    # RUN CHESS ENGINE
    def runEngine(self,view):
        
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

        view.runGame(self.gameLogic.board)
    
    # PlAY HUMAN MOVE
    def didTakeInput(self,move):

        # TELL GAMELOGIC to MAKE the MOVE if VALID
        if self.gameLogic.movePiece(move):
            # SHOW OUTPUT on VIEW
            self.outputHandler.output(move)
        else:
            # CANCEL MOVE on VIEW (PUT PIECE DOWN)
            self.outputHandler.cancelMove()
