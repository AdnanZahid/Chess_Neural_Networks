from src.models.pieces.piece import *
from src.models.squares import *
from src.others.constants import *


# This class handles all the king logic
class King(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.king

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_king
            self.fenSymbol = FENSymbols.white_king
        else:
            self.symbol = Symbols.black_king
            self.fenSymbol = FENSymbols.black_king

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

    def canMovePiece(self, board, toSquare, player=None, isCheckForCastling=True):

        # Add castling directions
        self.directionsList.append((2, 0))
        self.directionsList.append((-2, 0))

        wasCastlingSuccessful = False
        if player.king and board.checkIfSquareIsEmpty(toSquare) and player:

            if isCheckForCastling:
                if toSquare == Square(G1.file, self.position.rank) and player.isKingSideCastlingPossible():
                    board.castledRook = player.kingSideRook
                    wasCastlingSuccessful = super().canMovePiece(board, toSquare)
                elif toSquare == Square(C1.file, self.position.rank) and player.isQueenSideCastlingPossible():
                    board.castledRook = player.queenSideRook
                    wasCastlingSuccessful = super().canMovePiece(board, toSquare)

        # Remove castling directions (all occurences)
        self.directionsList = Utility.removeAllOccurencesFromList(self.directionsList, (2, 0))
        self.directionsList = Utility.removeAllOccurencesFromList(self.directionsList, (-2, 0))

        if wasCastlingSuccessful:
            player.lastMoveType = MoveType.castling
            return wasCastlingSuccessful
        else:
            player.lastMoveType = MoveType.normal
            return super().canMovePiece(board, toSquare)
