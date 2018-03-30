from src.others.move_generator import *


# This class represents all the player information (while and black)
class Player:

    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.piecesList = self.board.setupPieceBoard(color, self)
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
        return set(MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, self, isCheckForCheck=False))

    def isUnderCheck(self, board, king=None):
        # A quick hack to check for new king which is different from original king
        if king == None:
            king = self.king
        # Think twice before using isCanTakeKing=True!
        for move in MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, self.opponent, isCheckForCheck=False,
                                                                            isCanTakeKing=True):
            if move == king.position:
                return True
        return False

    def isUnderCheckMate(self, board):
        if self.isUnderCheck(board):
            for move in self.getAllPossibleTargetSquares(board):
                for piece in self.piecesList:
                    newBoard = copy.deepcopy(board)
                    newPiece = copy.deepcopy(piece)
                    newPiece.board = newBoard
                    for targetSquare in MoveGenerator.generatePossibleTargetSquares(piece, newBoard, self):
                        if MoveGenerator.canMovePiece(newPiece, newBoard, self, targetSquare):
                            if newBoard.movePiece(newPiece, targetSquare):
                                newPiece.updatePosition(targetSquare)
                                # A quick hack to check for new king which is different from original king
                                if newPiece.value == Values.king:
                                    newKing = newPiece
                                else:
                                    newKing = self.king
                                if not (self.isUnderCheck(newBoard, newKing)):
                                    return False
            return True
        return False

    def __repr__(self):
        if self.color == Color.white:
            return "White"
        else:
            return "Black"
