import copy

from src.models.pieces.pawn import *
from src.others.error_handler import *


# This class handles all the Board related tasks
class MoveGenerator:

    @staticmethod
    def getTotalMobility(board, player):
        return len(MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, player))

    @staticmethod
    def getMobility(piece, board, player):
        return len(MoveGenerator.generatePossibleTargetSquares(piece, board, player))

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquaresForAllPieces(board, player, isCheckForCheck=True, isCanTakeKing=False):
        possibleMovesToSquaresList = []

        for piece in player.piecesList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquares(piece, board, player, isCheckForCheck, isCanTakeKing))

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquares(piece, board, player, isCheckForCheck=True, isCanTakeKing=False):
        possibleMovesToSquaresList = []

        for direction in piece.directionsList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquaresInDirection(piece, board, player, direction, isCheckForCheck,
                                                                       isCanTakeKing))

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquaresInDirection(piece, board, player, direction, isCheckForCheck=True,
                                                 isCanTakeKing=False):
        if piece.strategy == Strategy.jumping:
            return MoveGenerator.generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, direction,
                                                                                   isCheckForCheck, isCanTakeKing)
        else:
            return MoveGenerator.generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, direction,
                                                                                   isCheckForCheck, isCanTakeKing)

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True,
                                                          isCanTakeKing=False):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        if MoveGenerator.canMove(piece, board, player, newPosition, isCheckForCheck, isCanTakeKing):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True,
                                                          isCanTakeKing=False):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        while MoveGenerator.canMove(piece, board, player, newPosition, isCheckForCheck, isCanTakeKing):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def canMove(piece, board, player, toSquare, isCheckForCheck=True, isCanTakeKing=False):
        result = False
        # STARTING and ENDING squares are not the same
        if not (piece.position == toSquare):
            # PIECE is not EMPTY or OUT OF BOUNDS
            if not (piece == EmptyPiece or piece == None):
                # This PIECE COLOR has the CURRENT TURN
                if piece.color == player.color:
                    # Check if PIECE can MOVE
                    if piece.canMove(board, toSquare):
                        # Can not go out of bounds
                        try:
                            existingPiece = board.grid[toSquare.rank][toSquare.file]
                        except IndexError:
                            existingPiece = None

                        if not (existingPiece == None):
                            # King can not be captured (unless isCanTakeKing is True)
                            # Think twice before using isCanTakeKing=True!
                            if existingPiece == EmptyPiece or not (existingPiece.value == Values.king) or isCanTakeKing:
                                # Destination square is empty
                                # And no friendly fire
                                if existingPiece == EmptyPiece \
                                        or not (existingPiece.color == piece.color):
                                    if not (piece == EmptyPiece):
                                        existingPiece.captured = True
                                        if isCheckForCheck:
                                            # Before checking for check
                                            # Make a move on a new board (clone of current one)
                                            # And then check if the player is under check or not
                                            newBoard = copy.deepcopy(board)
                                            newPiece = copy.deepcopy(piece)
                                            newPiece.board = newBoard
                                            newBoard.movePiece(newPiece, toSquare)
                                            newPiece.updatePosition(toSquare)
                                            result = not (player.isUnderCheck(newBoard))
                                        else:
                                            result = True
                                else:
                                    ErrorHandler.logError(board, piece, toSquare, Error.friendlyFire)
                            else:
                                ErrorHandler.logError(board, piece, toSquare, Error.kingCapture)
                        else:
                            ErrorHandler.logError(board, piece, toSquare, Error.invalidDestination)
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
            result = result or MoveGenerator.canCastle(piece, board, player, toSquare, result)

        return result

    @staticmethod
    def canMovePawn(piece, board, toSquare):

        result = False
        targetPiece = board.getPieceOnPosition(toSquare)
        # Simple 1 step or 2 step moves
        if board.checkIfSquareIsEmpty(toSquare):
            enpassantPiece = board.getPieceOnPosition(toSquare - (0, Pawn.pawnMoveDirection(piece.color, 1)))
            if Utility.getFileAndRankAdvance(EvaluationMove(piece.position, toSquare)) == piece.directionsList[0]:
                result = True
            elif Utility.getFileAndRankAdvance(EvaluationMove(piece.position, toSquare)) == piece.directionsList[1] \
                    and piece.hasMoved == False:
                result = board.checkForClearPath(EvaluationMove(piece.position, toSquare))
            #######################################################
            # Start of enpassant case (if enpassant piece exists) #
            #######################################################
            elif not (enpassantPiece == None) and not (enpassantPiece.color == piece.color):
                fileAndRankAdvance = Utility.getFileAndRankAdvance(
                    EvaluationMove(piece.position, toSquare))
                result = fileAndRankAdvance == piece.directionsList[2] or fileAndRankAdvance == piece.directionsList[3]
            #####################################################
            # End of enpassant case (if enpassant piece exists) #
            #####################################################
        # Simple capture (works only if target piece exists and is of opposite color)
        elif not (targetPiece == None) and not (targetPiece.color == piece.color):
            fileAndRankAdvance = Utility.getFileAndRankAdvance(EvaluationMove(piece.position, toSquare))
            result = fileAndRankAdvance == piece.directionsList[2] or fileAndRankAdvance == piece.directionsList[3]

        return result

    @staticmethod
    def canCastle(piece, board, player, toSquare, kingMoveResult):
        if kingMoveResult and board.getPieceOnPosition(toSquare) == None:

            kingSideRookPositionBeforeCastling = toSquare + (1, 0)
            queenSideRookPositionBeforeCastling = toSquare - (2, 0)
            kingSideRookPositionAfterCastling = toSquare - (1, 0)
            queenSideRookPositionAfterCastling = toSquare + (1, 0)

            if player.kingSideRook.position == toSquare + (1, 0):
                rook = player.kingSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    return player.kingSideRook.canMove(board, kingSideRookPositionAfterCastling)
            elif player.queenSideRook.position == toSquare - (2, 0):
                rook = player.queenSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    return player.queenSideRook.canMove(board, queenSideRookPositionAfterCastling)

        return False
