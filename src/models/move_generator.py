from src.others.constants import *
from src.others.error_handler import *
from src.others.utility import *


# This class handles all the Board related tasks
class MoveGenerator:

    @staticmethod
    def getTotalMobility(board, player):
        return len(MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, player))

    @staticmethod
    def getMobility(piece, board, player):
        return len(MoveGenerator.generatePossibleTargetSquares(piece, board, player))

    @staticmethod
    def generatePossibleTargetSquaresForAllPieces(board, player, isCheckForCheck=True):
        possibleMovesToSquaresList = []

        for piece in player.piecesList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquares(piece, board, player, isCheckForCheck))

        return possibleMovesToSquaresList

    @staticmethod
    def generatePossibleTargetSquares(piece, board, player, isCheckForCheck=True):
        possibleMovesToSquaresList = []

        for direction in piece.directionsList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquaresInDirection(piece, board, player, direction, isCheckForCheck))

        return possibleMovesToSquaresList

    @staticmethod
    def generatePossibleTargetSquaresInDirection(piece, board, player, direction, isCheckForCheck=True):
        if piece.value == Values.knight:
            return MoveGenerator.generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, direction, isCheckForCheck)
        else:
            return MoveGenerator.generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, direction, isCheckForCheck)

    @staticmethod
    def generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        if MoveGenerator.canMove(piece, board, player, newPosition, isCheckForCheck):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    def generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        while MoveGenerator.canMove(piece, board, player, newPosition, isCheckForCheck):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    def canMove(piece, board, player, toSquare, isCheckForCheck=True):

        result = False

        # STARTING and ENDING squares are not the same
        if not (piece.position == toSquare):

            # PIECE is not EMPTY or OUT OF BOUNDS
            if not (piece == EmptyPiece or piece == None):

                # This PIECE COLOR has the CURRENT TURN
                if piece.color == player.color:

                    # Check if PIECE can MOVE
                    if piece.canMove(board, toSquare):
                        if isCheckForCheck:
                            result = not (player.isUnderCheck(board))
                        else:
                            result = True
                    else:
                        ErrorHandler.logError(board, piece, toSquare, Error.invalidMove)
                else:
                    ErrorHandler.logError(board, piece, toSquare, Error.wrongTurn)
            else:
                ErrorHandler.logError(board, piece, toSquare, Error.invalidPiece)
        else:
            ErrorHandler.logError(board, piece, toSquare, Error.samePosition)

        # Pawn and king logic is handled separately because they depend on other pieces too
        # Such as normal pawn moves, enpassant and castling
        if piece.value == Values.pawn:
            result = result and MoveGenerator.canMovePawn(piece, board, toSquare)
        elif piece.value == Values.king:
            result = result and MoveGenerator.canCastle(piece, board, player, toSquare)

        return result

    @staticmethod
    def canMovePawn(piece, board, toSquare):

        result = False
        targetPiece = board.getPieceOnPosition(toSquare)
        if board.checkIfSquareIsEmpty(toSquare):
            if getFileAndRankAdvance(EvaluationMove(piece.position, toSquare)) == piece.directionsList[0]:
                result = True
            elif getFileAndRankAdvance(EvaluationMove(piece.position, toSquare)) == piece.directionsList[1] \
                    and piece.hasMoved == False:
                result = board.checkForClearPath(EvaluationMove(piece.position, toSquare))
        elif not (targetPiece == None) and not (targetPiece.color == piece.color):
            fileAndRankAdvance = getFileAndRankAdvance(EvaluationMove(piece.position, toSquare))
            result = fileAndRankAdvance == piece.directionsList[2] or fileAndRankAdvance == piece.directionsList[3]

        return result

    @staticmethod
    def canCastle(piece, board, player, toSquare):
        if player.kingSideRook.position == toSquare - (1, 0):
            rook = player.kingSideRook
            if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                return True
        elif player.queenSideRook.position == toSquare + (2, 0):
            rook = player.queenSideRook
            if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                return True

        return False
