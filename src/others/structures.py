# Here are all the basic structures
class EvaluationMove:
    def __init__(self,fromSquare,toSquare):
        self.fromSquare = fromSquare
        self.toSquare = toSquare

    # def __init__(self,fromSquare,toSquare,evaluationValue):
    #     self.fromSquare = fromSquare
    #     self.toSquare = toSquare
    #     self.evaluationValue = evaluationValue

class PieceState:
    def __init__(self,piece,position,hasMoved):
        self.piece = piece
        self.position = position
        self.hasMoved = hasMoved

class MoveState:
    def __init__(self,fromPieceState,toPieceState):
        self.fromPieceState = fromPieceState
        self.toPieceState = toPieceState

class RankIndex:
    k__2,k__1,k1,k2,k3,k4,k5,k6,k7,k8,k_1,k_2 = range(12)

class FileIndex:
    k__2,k__1,kA,kB,kC,kD,kE,kF,kG,kH,k_1,k_2 = range(12)

class Color:
    white = 1
    black = -1

# RANK ENUMERATION for all squares on the board
allPiecesRankEnumeration = range(RankIndex.k1,RankIndex.k8+1)

# FILE ENUMERATION for all squares on the board
allPiecesFileEnumeration = range(FileIndex.kA,FileIndex.kH+1)

# RANK ENUMERATION for squares occupied by WHITE PIECES
whitePiecesRankEnumeration = range(RankIndex.k1,RankIndex.k2+1)

# RANK ENUMERATION for squares occupied by BLACK PIECES
blackPiecesRankEnumeration = range(RankIndex.k7,RankIndex.k8+1)
