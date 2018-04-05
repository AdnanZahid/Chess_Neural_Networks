from src.models.player import *
from src.others.evaluation_handler import *


# This class represents all the AI related logic
class AIPlayer(Player):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.isAI = True

    def generateMove(self):
        move = self.getBestMove(kMaxPlies, self, kMinPossibleNumber, kMaxPossibleNumber)
        return EvaluationMove(move.fromSquare, move.toSquare)

    def getBestMove(self, depth, player, alpha, beta):
        _, newBoard, newPlayer = Utility.getDeepCopies(None, self.board, self)
        bestMove = EvaluationMove(None, None, kMinPossibleNumber)
        for piece in player.piecesList:
            fromSquare = piece.position
            for toSquare in MoveGenerator.generatePossibleTargetSquares(piece, self.board, self):
                newPiece = Utility.getDeepCopy(piece)
                if MoveGenerator.movePiece(newPiece, newBoard, newPlayer, toSquare):
                    localAlpha = alpha
                    evaluationMove = EvaluationMove(fromSquare, toSquare,
                                                    -self.getBestMoveValue(depth - 1, player.opponent, -beta,
                                                                           -localAlpha))

                    if evaluationMove.evaluationValue > bestMove.evaluationValue:
                        bestMove = evaluationMove

                    if bestMove.evaluationValue >= beta:
                        break

                elif bestMove.evaluationValue > alpha:
                    pass

        return bestMove

    def getBestMoveValue(self, depth, player, alpha, beta):
        _, newBoard, newPlayer = Utility.getDeepCopies(None, self.board, self)
        if depth == 0:
            if player.color == Color.white:
                return EvaluationHandler.getTotalEvaluationValue(newBoard, newPlayer)
            else:
                return -EvaluationHandler.getTotalEvaluationValue(newBoard, newPlayer)

        bestEvaluationValue = EvaluationMove(None, None, kMinPossibleNumber).evaluationValue
        for piece in player.piecesList:
            for toSquare in MoveGenerator.generatePossibleTargetSquares(piece, self.board, self):
                newPiece = Utility.getDeepCopy(piece)
                if MoveGenerator.movePiece(newPiece, newBoard, newPlayer, toSquare):
                    localAlpha = alpha
                    evaluationValue = -self.getBestMoveValue(depth - 1, player.opponent, -beta, -localAlpha)

                    if evaluationValue > bestEvaluationValue:
                        bestEvaluationValue = evaluationValue

                    if bestEvaluationValue >= beta:
                        break

                elif bestEvaluationValue > alpha:
                    pass

        return bestEvaluationValue
