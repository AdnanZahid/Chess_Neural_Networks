from src.models.pieces.piece import *

# This class handles all sorts of errors centrally
class ErrorHandler:
    @staticmethod
    def logError(board,piece,toSquare,error):
        if not(piece == NilPiece or piece == EmptyPiece):
            print("{} to move".format(board.currentTurnColor))
            print("{} -> {}{}-{}{}: {}".format(piece.symbol,piece.position.file,piece.position.rank,toSquare.file,toSquare.rank,error))
            board.printBoard()
        else:
            print(error)

class Error:
    friendlyFire       = "Can not captured own piece"
    invalidMove        = "This move is not valid"
    invalidPiece       = "No piece is selected"
    invalidDestination = "Destination out of bounds"
    underCheck         = "Your king is under check"
    underCheckmate     = "Your king is under checkmate"
    samePosition       = "Starting and ending positions are same"
    wrongTurn          = "It is not your turn"
    kingCapture        = "King can never be captured"
    none               = ""
