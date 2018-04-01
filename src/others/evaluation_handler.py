from src.others.move_generator import *


# This class contains all evaluation related methods
class EvaluationHandler:

    @staticmethod
    def getTotalEvaluationValue(player):
        return EvaluationHandler.getEvaluationValue(player.piecesList, player) - EvaluationHandler.getEvaluationValue(
            player.opponent.piecesList, player.opponent)

    @staticmethod
    def getEvaluationValue(piecesList, player, board):
        # This evaluation function relies on:
        # 1. Piece values
        # 2. Mobility values
        pieceValues = 0
        mobilityValues = 0
        for piece in piecesList:
            if piece.captured == False:
                pieceValues += piece.value
                mobilityValues += MoveGenerator.getMobility(piece, board, player)

        return pieceValues + mobilityValues
