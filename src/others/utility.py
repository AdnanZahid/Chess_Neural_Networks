from src.others.structures import *

# This file contains basic utility functions
def fileAdvanceCheck(move):
    return not(move.fromSquare.file == move.toSquare.file)

def rankAdvanceCheck(move):
    return not(move.fromSquare.rank == move.toSquare.rank)

def fileAdvanceOnlyCheck(move):
    return fileAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare)) and not(rankAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare)))

def rankAdvanceOnlyCheck(move):
    return not(fileAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare))) and rankAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare))

def fileOrRankAdvanceExclusiveCheck(move):
    return not(fileAdvanceOnlyCheck(EvaluationMove(move.fromSquare,move.toSquare)) == rankAdvanceOnlyCheck(EvaluationMove(move.fromSquare,move.toSquare)))

def fileOrRankAdvanceBothCheck(move):
    return fileAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare)) and rankAdvanceCheck(EvaluationMove(move.fromSquare,move.toSquare))

def getFileAndRankAdvance(move):
    return (move.toSquare.file - move.fromSquare.file, move.toSquare.rank - move.fromSquare.rank)

def getFileAndRankSingleAdvance(fileRankPair):
    
    if fileRankPair[0] == 0:
        return (0, fileRankPair[1]/abs(fileRankPair[1]))
    
    if fileRankPair[1] == 0:
        return (fileRankPair[0]/abs(fileRankPair[0]), 0)
    
    return (fileRankPair[0]/abs(fileRankPair[0]), fileRankPair[1]/abs(fileRankPair[1]))
