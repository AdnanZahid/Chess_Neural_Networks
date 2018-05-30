from src.others.move_generator import *


# This class contains all evaluation related methods
class EvaluationHandler:

    @staticmethod
    def getTotalEvaluationValue(board, player):
        return EvaluationHandler.getEvaluationValue(board, player) - EvaluationHandler.getEvaluationValue(board,
                                                                                                          player.opponent)

    @staticmethod
    def getEvaluationValue(board, player):
        # This evaluation function relies on:
        # 1. Piece values
        # 2. Mobility values
        pieceValues = 0
        mobilityValues = 0
        for piece in player.piecesList:
            pieceValues += piece.value
            mobilityValues += MoveGenerator.getMobility(piece, board, player) * 10

        return pieceValues + mobilityValues
