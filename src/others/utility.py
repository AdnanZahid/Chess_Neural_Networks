from src.others.structures import *


# This file contains basic utility functions
class Utility:

    # This function checks if file was changed (rank may be changed too)
    @staticmethod
    def fileAdvanceCheck(move):
        return not (move.fromSquare.file == move.toSquare.file)

    # This function checks if rank was changed (file may be changed too)
    @staticmethod
    def rankAdvanceCheck(move):
        return not (move.fromSquare.rank == move.toSquare.rank)

    # This function checks if only file was changed
    @staticmethod
    def fileAdvanceOnlyCheck(move):
        return Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)) and not (
            Utility.rankAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)))

    # This function checks if only rank was changed
    @staticmethod
    def rankAdvanceOnlyCheck(move):
        return not (
            Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare))) and Utility.rankAdvanceCheck(
            EvaluationMove(move.fromSquare, move.toSquare))

    # This function checks if only rank or only file was changed
    @staticmethod
    def fileOrRankAdvanceExclusiveCheck(move):
        return not (Utility.fileAdvanceOnlyCheck(
            EvaluationMove(move.fromSquare, move.toSquare)) == Utility.rankAdvanceOnlyCheck(
            EvaluationMove(move.fromSquare, move.toSquare)))

    # This function checks if rank and file both were changed
    @staticmethod
    def fileOrRankAdvanceBothCheck(move):
        return Utility.fileAdvanceCheck(EvaluationMove(move.fromSquare, move.toSquare)) and Utility.rankAdvanceCheck(
            EvaluationMove(move.fromSquare, move.toSquare))

    # This function determines how many steps to take in X and Y direction to reach the final position given the starting position
    @staticmethod
    def getFileAndRankAdvance(move):
        return (move.toSquare.file - move.fromSquare.file, move.toSquare.rank - move.fromSquare.rank)

    # This function gets a single advance value in given direction - for example (1, 0) if fileRankPair is (7, 0)
    # More like simplifying a fraction or dividing by absolute GCD
    @staticmethod
    def getFileAndRankSingleAdvance(fileRankPair):
        # Compute absolute GCD
        gcd = Utility.absoluteGCD(fileRankPair[0], fileRankPair[1])
        # This will only happen in case of (0, 0)
        if gcd == 0:
            return 0, 0
        # Return simplified fraction or simplest direction given the actual direction
        return fileRankPair[0] // gcd, fileRankPair[1] // gcd

    # This function determines if the move was made in the right direction
    @staticmethod
    def isMoveInCorrectDirection(move, directionsList, strategy):
        # Direction in which the move is taken

        # If strategy is jumping, just take the file and rank advance
        # Otherwise if it is sliding, take only single advance in that direction
        if strategy == Strategy.jumping:
            moveDirection = Utility.getFileAndRankAdvance(move)
        else:
            moveDirection = Utility.getFileAndRankSingleAdvance(Utility.getFileAndRankAdvance(move))
        # Iterate over the directions list, even if one value matches return True
        for direction in directionsList:
            if direction == moveDirection:
                return True
        return False

    @staticmethod
    def absoluteGCD(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def removeAllOccurencesFromList(list, valueToRemove):
        return [value for value in list if not (value == valueToRemove)]
