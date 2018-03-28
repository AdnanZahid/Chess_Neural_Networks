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

        # Castling directions
        self.directionsList.append((2, 0))
        self.directionsList.append((-2, 0))

    def canMove(self, board, toSquare, player=None):

        result = False
        if board.getPieceOnPosition(toSquare) == None and not (player == None):

            kingSideRookPositionBeforeCastling = toSquare + (1, 0)
            queenSideRookPositionBeforeCastling = toSquare - (2, 0)
            kingSideRookPositionAfterCastling = toSquare - (1, 0)
            queenSideRookPositionAfterCastling = toSquare + (1, 0)

            if player.kingSideRook.position == toSquare + (1, 0):
                rook = player.kingSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    result = player.kingSideRook.canMove(board, kingSideRookPositionAfterCastling) and super().canMove(board, toSquare)
            elif player.queenSideRook.position == toSquare - (2, 0):
                rook = player.queenSideRook
                if not (player.king.hasMoved) and not (rook.hasMoved) and not (rook.captured):
                    result = player.queenSideRook.canMove(board, queenSideRookPositionAfterCastling) and super().canMove(board, toSquare)

        move = EvaluationMove(self.position, toSquare)
        return result or super().canMove(board, toSquare)
