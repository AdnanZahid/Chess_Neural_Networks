from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the pawn logic
class Pawn(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.pawn

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_pawn
        else:
            self.symbol = Symbols.black_pawn

        # Pawn directions

        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, self.pawnMoveDirection(1)))
        self.directionsList.append((0, self.pawnMoveDirection(2)))

        self.directionsList.append((-1, self.pawnMoveDirection(1)))
        self.directionsList.append((1, self.pawnMoveDirection(1)))

    def canMove(self, board, toSquare, player=None):

        result = False
        targetPiece = board.getPieceOnPosition(toSquare)
        # Simple 1 step or 2 step moves
        if board.checkIfSquareIsEmpty(toSquare):
            enpassantPiece = board.getPieceOnPosition(toSquare - (0, self.pawnMoveDirection(1)))
            if Utility.getFileAndRankAdvance(EvaluationMove(self.position, toSquare)) == self.directionsList[0]:
                result = True
            elif Utility.getFileAndRankAdvance(EvaluationMove(self.position, toSquare)) == self.directionsList[1] \
                    and self.hasMoved == False:
                result = board.checkForClearPath(EvaluationMove(self.position, toSquare))
            #######################################################
            # Start of enpassant case (if enpassant piece exists) #
            #######################################################
            elif not (enpassantPiece == None) and not (enpassantPiece.color == self.color):
                fileAndRankAdvance = Utility.getFileAndRankAdvance(
                    EvaluationMove(self.position, toSquare))
                result = fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]
            #####################################################
            # End of enpassant case (if enpassant piece exists) #
            #####################################################
        # Simple capture (works only if target piece exists and is of opposite color)
        elif not (targetPiece == None) and not (targetPiece.color == self.color):
            fileAndRankAdvance = Utility.getFileAndRankAdvance(EvaluationMove(self.position, toSquare))
            result = fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]

        move = EvaluationMove(self.position, toSquare)
        return result and super().canMove(board, toSquare)

    def pawnMoveDirection(self, number):
        return self.color * number
