from src.models.pieces.strategies.move_strategy import *


class LimitedMoveStrategy(MoveStrategy):

    def generatePossibleTargetSquare(self, position, fileRankPair):
        possibleMovesToSquaresList = []
        newPosition = position + fileRankPair

        if self.piece.moveToSquare(newPosition):
            possibleMovesToSquaresList.append(newPosition)

        return possibleMovesToSquaresList
