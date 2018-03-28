import copy

from src.models.squares import *
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
        directionsList = piece.directionsList

        if piece.value == Values.king:
            # Add castling directions
            directionsList.append((2, 0))
            directionsList.append((-2, 0))

        for direction in directionsList:
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

        if MoveGenerator.canMovePiece(piece, board, player, newPosition, isCheckForCheck, isCanTakeKing):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True,
                                                          isCanTakeKing=False):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        while MoveGenerator.canMovePiece(piece, board, player, newPosition, isCheckForCheck, isCanTakeKing):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    # Think twice before using isCanTakeKing=True!
    def canMovePiece(piece, board, player, toSquare, isCheckForCheck=True, isCanTakeKing=False):
        result = False
        # STARTING and ENDING squares are not the same
        if not (piece.position == toSquare):
            # PIECE is not EMPTY or OUT OF BOUNDS
            if not (piece == EmptyPiece or piece == None):
                # This PIECE COLOR has the CURRENT TURN
                if piece.color == player.color:
                    # Check if PIECE can MOVE
                    if piece.canMovePiece(board, toSquare, player):
                        # Can not go out of bounds
                        try:
                            existingPiece = board.grid[toSquare.rank][toSquare.file]
                        except IndexError:
                            existingPiece = None

                        if existingPiece:
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
                                    if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare,
                                                                              Error.friendlyFire)
                            else:
                                if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.kingCapture)
                        else:
                            if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.invalidDestination)
                    else:
                        if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.invalidMove)
                else:
                    if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.wrongTurn)
            else:
                if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.invalidPiece)
        else:
            if isCheckForCheck: ErrorHandler.logError(board, piece, toSquare, Error.samePosition)

        return result

    @staticmethod
    def movePiece(piece, board, player, toSquare):
        if MoveGenerator.canMovePiece(piece, board, player, toSquare):
            if board.movePiece(piece, toSquare, player):
                piece.updatePosition(toSquare)

                # If moved pawn exists (enpassant pawn), remove it (capture it)
                if player.lastMoveType == MoveType.enpassant:
                    if board.movedPawn:
                        board.putEmptyPieceOnPosition(board.movedPawn.position)
                        board.movedPawn = None

                # If castled rook exists, move it next to king - in other words complete caslting
                elif player.lastMoveType == MoveType.castling:
                    castledRook = board.castledRook
                    if castledRook:
                        # Put the rook at at an appropriate position after castling
                        if player.kingSideRook == castledRook:
                            castledRookUpdatedPosition = Square(FileIndex.kF, castledRook.position.rank)
                            board.putPieceOnPosition(castledRook, castledRookUpdatedPosition)
                        elif player.queenSideRook == castledRook:
                            castledRookUpdatedPosition = Square(FileIndex.kD, castledRook.position.rank)
                            board.putPieceOnPosition(castledRook, castledRookUpdatedPosition)
                        # Put an empty piece in place of rook
                        board.putEmptyPieceOnPosition(castledRook.position)
                        board.castledRook = None
                        castledRook.updatePosition(castledRookUpdatedPosition)

                # If the piece moved is pawn
                # Store it in moved pawn property
                if piece.value == Values.pawn:
                    board.movedPawn = piece
                else:
                    board.movedPawn = None

                return True
        return False
