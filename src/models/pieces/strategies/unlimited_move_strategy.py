from src.models.pieces.strategies.move_strategy import *


class UnlimitedMoveStrategy(MoveStrategy):

    def generatePossibleTargetSquare(self, position, fileRankPair):
        possibleMovesToSquaresList = []
        newPosition = position + fileRankPair

        while self.piece.moveToSquare(newPosition):
            possibleMovesToSquaresList.append(newPosition)
            newPosition = newPosition + fileRankPair

        return possibleMovesToSquaresList
