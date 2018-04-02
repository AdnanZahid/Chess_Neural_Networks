from src.models.player import *
from src.others.evaluation_handler import *


# This class represents all the AI related logic
class AIPlayer(Player):

    def __init__(self, color, board):
        self.isAI = True
        super().__init__(color, board)

    def generateMove(self):
        move = self.getBestMove(kMaxPlies, self, int.min / 2, int.max / 2)
        return EvaluationMove(move.fromSquare, move.toSquare)

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
                    Move = EvaluationMove(fromSquare, toSquare,
                                          -self.getBestMove(depth - 1, player.opponent, -beta,
                                                            -localAlpha))

                    if Move.evaluationValue > bestMove.evaluationValue:
                        bestMove = Move

                    if bestMove.evaluationValue >= beta:
                        break

                elif bestMove.evaluationValue > alpha:
                    pass

        return bestMove
