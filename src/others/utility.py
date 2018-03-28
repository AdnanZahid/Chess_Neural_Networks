from src.others.structures import *


# This file contains basic utility functions
class Utility:

    @staticmethod
    def fileAdvanceCheck(move):
        return not (move.fromSquare.file == move.toSquare.file)

    @staticmethod
    def rankAdvanceCheck(move):
        return not (move.fromSquare.rank == move.toSquare.rank)

    @staticmethod
    def fileAdvanceOnlyCheck(move):
        return Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)) and not (
            Utility.rankAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)))

    @staticmethod
    def rankAdvanceOnlyCheck(move):
        return not (
            Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare))) and Utility.rankAdvanceCheck(
            EvaluationMove(move.fromSquare, move.toSquare))

    @staticmethod
    def fileOrRankAdvanceExclusiveCheck(move):
        return not (Utility.fileAdvanceOnlyCheck(
            EvaluationMove(move.fromSquare, move.toSquare)) == Utility.rankAdvanceOnlyCheck(
            EvaluationMove(move.fromSquare, move.toSquare)))

    @staticmethod
    def fileOrRankAdvanceBothCheck(move):
        return Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)) and Utility.rankAdvanceCheck(
            EvaluationMove(move.fromSquare, move.toSquare))

    @staticmethod
    def getFileAndRankAdvance(move):
        return (move.toSquare.file - move.fromSquare.file, move.toSquare.rank - move.fromSquare.rank)

    # This gets a single advance value in given direction - for example (1, 0) if fileRankPair is (7, 0)
    @staticmethod
    def getFileAndRankSingleAdvance(fileRankPair):

        if fileRankPair[0] == 0 and fileRankPair[1] == 0:
            return (0, 0)

        if fileRankPair[0] == 0:
            return (0, fileRankPair[1] // abs(fileRankPair[1]))

        if fileRankPair[1] == 0:
            return (fileRankPair[0] // abs(fileRankPair[0]), 0)

        return (fileRankPair[0] // abs(fileRankPair[0]), fileRankPair[1] // abs(fileRankPair[1]))

    # This checks if move is in correct direction
    # By checking if there are no remainders
    @staticmethod
    def isMoveInCorrectDirection(move, directionsList):
        isDirectionCorrect = False
        for direction in directionsList:
            if Utility.getFileAndRankAdvance(move)[0] % direction[0] == 0 and Utility.getFileAndRankAdvance(move)[1] % \
                    direction[1] == 0:
                isDirectionCorrect = True
                break
        return isDirectionCorrect
