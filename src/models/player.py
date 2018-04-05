from abc import abstractmethod

from src.others.move_generator import *


# This class represents all the player information (while and black)
class Player:

    def __init__(self, color, board):
        self.isAI = False
        self.color = color
        self.board = board
        self.piecesList = self.board.setupPieceBoard(color)
        # Will be used to determine whether the last move was enpassant or castling
        self.lastMoveType = None

        for piece in self.piecesList:
            if piece.value == Values.king:
                # Set king property of player for later use (castling, check and checkmate)
                self.king = piece
            elif piece.value == Values.rook:
                # Set king(H file)/queen(A file) side rook property of player for later use (castling)
                if piece.position.file == FileIndex.kH:
                    self.kingSideRook = piece
                else:
                    self.queenSideRook = piece

    def clearPlayerData(self):
        self.piecesList = []
        self.king = None
        self.kingSideRook = None
        self.kingSideRook = None

    def move(self, move):
        piece = self.board.getPieceOnPosition(move.fromSquare)
        return MoveGenerator.movePiece(piece, self.board, self, move.toSquare)

    def getAllPossibleTargetSquares(self, board):
        return MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, self, isCheckForCheck=False)

    def isUnderCheck(self, board, position=None):
        # A quick hack to check for new king position which is different from original king
        if not (position) and self.king:
            position = self.king.position

        return position in self.opponent.getAllPossibleTargetSquares(board)

    def isUnderCheckMate(self, board):
        _, newBoard, newPlayer = Utility.getDeepCopies(None, board, self)
        if newPlayer.isUnderCheck(board):
            for piece in self.piecesList:
                newPiece = Utility.getDeepCopy(piece)
                for targetSquare in MoveGenerator.generatePossibleTargetSquares(piece, newBoard, newPlayer):
                    if MoveGenerator.movePiece(newPiece, newBoard, newPlayer, targetSquare):
                        newPiece.updatePosition(targetSquare)
                        # A quick hack to check for new king position which is different from original king
                        if newPiece.value == Values.king:
                            newKing = newPiece
                        else:
                            newKing = self.king
                        if not (newPlayer.isUnderCheck(newBoard, newKing.position)):
                            return False
            return True
        return False

    def isCastlingPossibleForRook(self,
                                  board,
                                  player,
                                  king,
                                  rook,
                                  rookPositionBeforeCastling,
                                  rookPositionAfterCastling,
                                  intermediateSquare):
        return rook \
               and rook.position == rookPositionBeforeCastling \
               and not (king.hasMoved) \
               and not (rook.hasMoved) \
               and rook.canMovePiece(board, rookPositionAfterCastling) \
               and not (player.isUnderCheck(board)) \
               and not (player.isUnderCheck(board, intermediateSquare))

    def isKingSideCastlingPossible(self):
        board = self.board
        player = self
        king = self.king
        rook = self.kingSideRook

        if player.color == Color.white:
            rookPositionBeforeCastling = H1
            rookPositionAfterCastling = F1
            intermediateSquare = F1
        else:
            rookPositionBeforeCastling = H8
            rookPositionAfterCastling = F8
            intermediateSquare = F8

        return player.isCastlingPossibleForRook(board,
                                                player,
                                                king,
                                                rook,
                                                rookPositionBeforeCastling,
                                                rookPositionAfterCastling,
                                                intermediateSquare)

    def isQueenSideCastlingPossible(self):
        board = self.board
        player = self
        king = self.king
        rook = self.queenSideRook

        if player.color == Color.white:
            rookPositionBeforeCastling = A1
            rookPositionAfterCastling = D1
            intermediateSquare = D1
        else:
            rookPositionBeforeCastling = A8
            rookPositionAfterCastling = D8
            intermediateSquare = D8

        return player.isCastlingPossibleForRook(board,
                                                player,
                                                king,
                                                rook,
                                                rookPositionBeforeCastling,
                                                rookPositionAfterCastling,
                                                intermediateSquare)

    def hasKingSideCastlingRights(self):
        return not (self.king.hasMoved) and not (self.kingSideRook.hasMoved)

    def hasQueenSideCastlingRights(self):
        return not (self.king.hasMoved) and not (self.queenSideRook.hasMoved)

    @abstractmethod
    def generateMove(self):
        pass

    def __repr__(self):
        if self.color == Color.white:
            return "White"
        else:
            return "Black"
