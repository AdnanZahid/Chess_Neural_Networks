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
    def generatePossibleTargetSquaresForAllPieces(board, player, isCheckForCheck=True):
        possibleMovesToSquaresList = []

        for piece in player.piecesList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquares(piece, board, player, isCheckForCheck))

        return set(possibleMovesToSquaresList)

    @staticmethod
    def generatePossibleTargetSquaresForFileAndRank(file, rank, board, player):
        piece = board.getPieceOnPosition(Square(file, rank))
        if Utility.isValidPiece(piece):
            return MoveGenerator.generatePossibleTargetSquares(piece, board, player)
        else:
            return []

    @staticmethod
    def generatePossibleTargetSquares(piece, board, player, isCheckForCheck=True):
        possibleMovesToSquaresList = []
        directionsList = piece.directionsList

        if piece.value == Values.king:
            # Add castling directions
            directionsList.append((2, 0))
            directionsList.append((-2, 0))

        for direction in directionsList:
            possibleMovesToSquaresList.extend(
                MoveGenerator.generatePossibleTargetSquaresInDirection(piece, board, player, direction,
                                                                       isCheckForCheck))

        return possibleMovesToSquaresList

    @staticmethod
    def generatePossibleTargetSquaresInDirection(piece, board, player, direction, isCheckForCheck=True):
        if piece.strategy == Strategy.jumping:
            return MoveGenerator.generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, direction,
                                                                                   isCheckForCheck)
        else:
            return MoveGenerator.generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, direction,
                                                                                   isCheckForCheck)

    @staticmethod
    def generatePossibleTargetSquaresByJumpingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        if board.getPieceOnPosition(newPosition):
            if MoveGenerator.canMovePiece(piece, board, player, newPosition, isCheckForCheck):
                possibleMovesToSquaresList.append(newPosition)

        return possibleMovesToSquaresList

    @staticmethod
    def generatePossibleTargetSquaresBySlidingInDirection(piece, board, player, fileRankPair, isCheckForCheck=True):
        possibleMovesToSquaresList = []
        newPosition = piece.position + fileRankPair

        while board.getPieceOnPosition(newPosition):
            if MoveGenerator.canMovePiece(piece, board, player, newPosition, isCheckForCheck):
                possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList

    @staticmethod
    def canMovePiece(piece, board, player, toSquare, isCheckForCheck=True):
        result = False
        # STARTING and ENDING squares are not the same
        if not (piece.position == toSquare):
            # PIECE is not EMPTY or OUT OF BOUNDS
            if Utility.isValidPiece(piece):
                # This PIECE COLOR has the CURRENT TURN
                if piece.color == player.color:
                    # Check if PIECE can MOVE
                    if piece.canMovePiece(board, toSquare, player, isCheckForCastling=isCheckForCheck):
                        # Can not go out of bounds
                        existingPiece = board.getPieceOnPosition(toSquare)
                        if existingPiece and Utility.isValidPiece(piece):
                            existingPiece.captured = True
                            if isCheckForCheck:
                                newPiece, newBoard, newPlayer = Utility.getDeepCopies(piece, board, player)
                                newBoard.movePiece(newPiece, toSquare, newPlayer)
                                newPiece.updatePosition(toSquare)
                                # A quick hack to check for new king position which is different from original king
                                newKing = None
                                if newPiece.value == Values.king:
                                    newKing = newPiece
                                if newKing:
                                    result = not (newPlayer.isUnderCheck(newBoard, newKing.position))
                                else:
                                    result = not (newPlayer.isUnderCheck(newBoard))
                            else:
                                result = True
                        else:
                            ErrorHandler.logError(piece, toSquare, Error.invalidDestination)
                    else:
                        ErrorHandler.logError(piece, toSquare, Error.invalidMove)
                else:
                    ErrorHandler.logError(piece, toSquare, Error.wrongTurn)
            else:
                ErrorHandler.logError(piece, toSquare, Error.invalidPiece)
        else:
            ErrorHandler.logError(piece, toSquare, Error.samePosition)

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
