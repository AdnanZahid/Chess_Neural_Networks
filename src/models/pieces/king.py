from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the king logic
class King(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.king

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_king
        else:
            self.symbol = Symbols.black_king

        # King directions

        # Normal king directions
        self.directionsList.append((1, 1))
        self.directionsList.append((1, -1))
        self.directionsList.append((-1, 1))
        self.directionsList.append((-1, -1))

        self.directionsList.append((1, 0))
        self.directionsList.append((0, 1))
        self.directionsList.append((-1, 0))
        self.directionsList.append((0, -1))

    def canMovePiece(self, board, toSquare, player=None):

        # Add castling directions
        self.directionsList.append((2, 0))
        self.directionsList.append((-2, 0))

        wasCastlingSuccessful = False
        if player.king and board.getPieceOnPosition(toSquare) == None and player:

            kingSideRookPositionBeforeCastling = toSquare + (1, 0)
            queenSideRookPositionBeforeCastling = toSquare - (2, 0)
            kingSideRookPositionAfterCastling = toSquare - (1, 0)
            queenSideRookPositionAfterCastling = toSquare + (1, 0)

            if player.kingSideRook and player.kingSideRook.position == toSquare + (1, 0):
                rook = player.kingSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    if player.kingSideRook.canMovePiece(board, kingSideRookPositionAfterCastling):
                        if super().canMovePiece(board, toSquare):
                            board.castledRook = player.kingSideRook
                            wasCastlingSuccessful = True
            elif player.queenSideRook and player.queenSideRook.position == toSquare - (2, 0):
                rook = player.queenSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    if player.queenSideRook.canMovePiece(board, queenSideRookPositionAfterCastling):
                        if super().canMovePiece(board, toSquare):
                            board.castledRook = player.queenSideRook
                            wasCastlingSuccessful = True

        # Remove castling directions (all occurences)
        self.directionsList = Utility.removeAllOccurencesFromList(self.directionsList, (2, 0))
        self.directionsList = Utility.removeAllOccurencesFromList(self.directionsList, (-2, 0))

        if wasCastlingSuccessful:
            player.lastMoveType = MoveType.castling
            return wasCastlingSuccessful
        else:
            player.lastMoveType = MoveType.normal
            return super().canMovePiece(board, toSquare)
