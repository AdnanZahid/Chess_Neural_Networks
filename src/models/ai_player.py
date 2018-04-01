from src.models.player import *


# This class represents all the AI related logic
class AIPlayer(Player):

    def __init__(self, color, board):
        super().__init__(color, board)

    def firstAlphaBeta(depth, player, alpha, beta):
        bestMove = EvaluationMove(None, None, Int.min)
        for piece in player.piecesList:
            if piece.captured == False:
                fromSquare = piece.position
                for toSquare in MoveGenerator.generatePossibleTargetSquares(piece, self.board, self):
                    if MoveGenerator.movePiece(piece, self.board, self, toSquare):
                        localAlpha = alpha
                        evaluationMove = EvaluationMove(fromSquare, toSquare, evaluationValue: -alphaBeta(depth - 1, player.opponent!, alpha: -beta, beta: -localAlpha))

                        if evaluationMove.evaluationValue > bestMove.evaluationValue:
                            bestMove = evaluationMove

                        if bestMove.evaluationValue >= beta:
                            break

                    elif bestMove.evaluationValue > alpha:
                        localAlpha = bestMove.evaluationValue

        return bestMove

    def alphaBeta(depth, player, alpha, beta):

        if depth == 0:
            if player.color == Color.white:
                return self.board.evaluationValue
            else:
                return -self.board.evaluationValue

        bestEvaluationValue = int.min / 2

        for piece in player.piecesList:
            if piece.captured == False:
                fromSquare = piece.position

                for toSquare in MoveGenerator.generatePossibleTargetSquares(piece, self.board, self):

                    if MoveGenerator.movePiece(piece, self.board, self, toSquare):
                        localAlpha = alpha
                        evaluationValue = -self.alphaBeta(depth - 1, player.opponent, alpha: -beta, beta: -localAlpha)

                        if evaluationValue > bestEvaluationValue:
                            bestEvaluationValue = evaluationValue

                        if bestEvaluationValue >= beta:
                            break

                        elif bestEvaluationValue > alpha:
                            localAlpha = bestEvaluationValue

        return bestEvaluationValue
