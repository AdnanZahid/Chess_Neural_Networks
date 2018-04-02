from src.models.player import *
from src.others.evaluation_handler import *


# This class represents all the AI related logic
class AIPlayer(Player):

    def __init__(self, color, board):
        super().__init__(color, board)

    def getBestMove(self, depth, player, alpha, beta):
        if depth == 0:
            if player.color == Color.white:
                return EvaluationHandler(self, self.board)
            else:
                return -EvaluationHandler(self, self.board)

        bestMove = EvaluationMove(None, None, int.min)
        for piece in player.piecesList:
            fromSquare = piece.position
            for toSquare in MoveGenerator.generatePossibleTargetSquares(piece, self.board, self):
                if MoveGenerator.movePiece(piece, self.board, self, toSquare):
                    localAlpha = alpha
                    evaluationMove = EvaluationMove(fromSquare, toSquare,
                                                    -self.getBestMove(depth - 1, player.opponent, -beta,
                                                                      -localAlpha))

                    if evaluationMove.evaluationValue > bestMove.evaluationValue:
                        bestMove = evaluationMove

                    if bestMove.evaluationValue >= beta:
                        break

                elif bestMove.evaluationValue > alpha:
                    pass

        return bestMove
