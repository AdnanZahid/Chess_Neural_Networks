import copy

from src.others.structures import *


# This class represents all the player information (while and black)
class Player:

    def __init__(self, color, board, gameLogic):
        self.color = color
        self.board = board
        self.gameLogic = gameLogic
        self.piecesList = self.board.setupPieceBoard(color, self)

    def movePiece(self, move, checkCurrentTurn=True):
        result = False

        if self.board.movePiece(move, checkCurrentTurn):
            result = True

        return result

    def setKing(self, king):
        self.king = king

    def setKingSideRook(self, rook):
        self.kingSideRook = rook

    def setQueenSideRook(self, rook):
        self.queenSideRook = rook

    def getAllPossibleTargetSquares(self, board = None):
        movesList = []
        for piece in self.piecesList:
            # Replace the board in current piece if it exists
            if board:
                piece.board = board
            movesList.extend(piece.moveStrategy.generateAllPossibleTargetSquares(False))
            piece.board = self.board
        return movesList

    def isUnderCheck(self, board = None):
        for move in self.opponent.getAllPossibleTargetSquares(board):
            if move == self.king.position:
                return True
        return False

    def isUnderCheckMate(self):
        result = self.isUnderCheck()
        if result:
            for move in self.getAllPossibleTargetSquares():
                for piece in self.piecesList:
                    newBoard = copy.deepcopy(self.board)
                    newPiece = copy.deepcopy(piece)
                    newPiece.board = newBoard
                    for targetSquare in piece.moveStrategy.generateAllPossibleTargetSquares():
                        if newBoard.movePiece(EvaluationMove(newPiece.position, targetSquare), True):
                            result = result and self.isUnderCheck()
        return result

    def isUnderCheckOnNewBoard(self, piece, toSquare):
        newBoard = copy.deepcopy(self.board)
        newPiece = copy.deepcopy(piece)
        newPiece.board = newBoard

        isUnderCheck = True
        if newBoard.putEmptyPieceOnPosition(newPiece.position):
            if newBoard.putPieceOnPosition(newPiece, toSquare, True):
                isUnderCheck = self.isUnderCheck(newBoard)

        return isUnderCheck
