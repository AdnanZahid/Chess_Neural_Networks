from src.others.constants import *
from src.others.structures import *


# This class represents a square and its essential functions
class Square:

    # Initialization from file and rank
    # File can either be number or alphabet
    def __init__(self, file, rank):

        if type(file) is int and type(rank) is int:
            # If file is number
            self.file = file
            self.rank = rank
        else:
            # If file is alphabet
            self.file = Square.convertAlphabetToNumber(file)
            self.rank = int(rank) - 1

        self.order = (self.rank * kNumberOfSquaresAlongRank) + self.file

    # Initialization from order
    @staticmethod
    def initializeFromOrder(order):
        square = Square(0, 0)
        square.file = order % kNumberOfSquaresAlongFile
        square.rank = order // kNumberOfSquaresAlongRank
        square.order = order
        return square

    def __eq__(self, other):
        return self.order == other.order

    def __hash__(self):
        return self.order

    def __add__(self, fileRankPair):
        return Square(self.file + fileRankPair[0], self.rank + fileRankPair[1])

    def __sub__(self, fileRankPair):
        return Square(self.file - fileRankPair[0], self.rank - fileRankPair[1])

    def __lt__(self, other):
        return self.order < other.order

    def __repr__(self):
        if Square.fileString(self.file) == "Invalid file" or self.rank < RankIndex.k1 or self.rank > RankIndex.k8:
            return "Invalid square"
        return "{}{}".format(Square.fileString(self.file), self.rank + 1)

    @staticmethod
    def convertAlphabetToNumber(alphabet):
        if len(alphabet) != 1:
            return 0
        number = ord(alphabet)
        if 65 <= number <= 90:
            # Upper case letter
            return number - 65
        elif 97 <= number <= 122:
            # Lower case letter
            return number - 97
        # Unrecognized character
        return 0

    @staticmethod
    def fileString(file):
        if file == FileIndex.kA:
            return "A"
        elif file == FileIndex.kB:
            return "B"
        elif file == FileIndex.kC:
            return "C"
        elif file == FileIndex.kD:
            return "D"
        elif file == FileIndex.kE:
            return "E"
        elif file == FileIndex.kF:
            return "F"
        elif file == FileIndex.kG:
            return "G"
        elif file == FileIndex.kH:
            return "H"
        else:
            return "Invalid file"


# This defines all board squares as global constants

A1 = Square(FileIndex.kA, RankIndex.k1)
A2 = Square(FileIndex.kA, RankIndex.k2)
A3 = Square(FileIndex.kA, RankIndex.k3)
A4 = Square(FileIndex.kA, RankIndex.k4)
A5 = Square(FileIndex.kA, RankIndex.k5)
A6 = Square(FileIndex.kA, RankIndex.k6)
A7 = Square(FileIndex.kA, RankIndex.k7)
A8 = Square(FileIndex.kA, RankIndex.k8)

B1 = Square(FileIndex.kB, RankIndex.k1)
B2 = Square(FileIndex.kB, RankIndex.k2)
B3 = Square(FileIndex.kB, RankIndex.k3)
B4 = Square(FileIndex.kB, RankIndex.k4)
B5 = Square(FileIndex.kB, RankIndex.k5)
B6 = Square(FileIndex.kB, RankIndex.k6)
B7 = Square(FileIndex.kB, RankIndex.k7)
B8 = Square(FileIndex.kB, RankIndex.k8)

C1 = Square(FileIndex.kC, RankIndex.k1)
C2 = Square(FileIndex.kC, RankIndex.k2)
C3 = Square(FileIndex.kC, RankIndex.k3)
C4 = Square(FileIndex.kC, RankIndex.k4)
C5 = Square(FileIndex.kC, RankIndex.k5)
C6 = Square(FileIndex.kC, RankIndex.k6)
C7 = Square(FileIndex.kC, RankIndex.k7)
C8 = Square(FileIndex.kC, RankIndex.k8)

D1 = Square(FileIndex.kD, RankIndex.k1)
D2 = Square(FileIndex.kD, RankIndex.k2)
D3 = Square(FileIndex.kD, RankIndex.k3)
D4 = Square(FileIndex.kD, RankIndex.k4)
D5 = Square(FileIndex.kD, RankIndex.k5)
D6 = Square(FileIndex.kD, RankIndex.k6)
D7 = Square(FileIndex.kD, RankIndex.k7)
D8 = Square(FileIndex.kD, RankIndex.k8)

E1 = Square(FileIndex.kE, RankIndex.k1)
E2 = Square(FileIndex.kE, RankIndex.k2)
E3 = Square(FileIndex.kE, RankIndex.k3)
E4 = Square(FileIndex.kE, RankIndex.k4)
E5 = Square(FileIndex.kE, RankIndex.k5)
E6 = Square(FileIndex.kE, RankIndex.k6)
E7 = Square(FileIndex.kE, RankIndex.k7)
E8 = Square(FileIndex.kE, RankIndex.k8)

F1 = Square(FileIndex.kF, RankIndex.k1)
F2 = Square(FileIndex.kF, RankIndex.k2)
F3 = Square(FileIndex.kF, RankIndex.k3)
F4 = Square(FileIndex.kF, RankIndex.k4)
F5 = Square(FileIndex.kF, RankIndex.k5)
F6 = Square(FileIndex.kF, RankIndex.k6)
F7 = Square(FileIndex.kF, RankIndex.k7)
F8 = Square(FileIndex.kF, RankIndex.k8)

G1 = Square(FileIndex.kG, RankIndex.k1)
G2 = Square(FileIndex.kG, RankIndex.k2)
G3 = Square(FileIndex.kG, RankIndex.k3)
G4 = Square(FileIndex.kG, RankIndex.k4)
G5 = Square(FileIndex.kG, RankIndex.k5)
G6 = Square(FileIndex.kG, RankIndex.k6)
G7 = Square(FileIndex.kG, RankIndex.k7)
G8 = Square(FileIndex.kG, RankIndex.k8)

H1 = Square(FileIndex.kH, RankIndex.k1)
H2 = Square(FileIndex.kH, RankIndex.k2)
H3 = Square(FileIndex.kH, RankIndex.k3)
H4 = Square(FileIndex.kH, RankIndex.k4)
H5 = Square(FileIndex.kH, RankIndex.k5)
H6 = Square(FileIndex.kH, RankIndex.k6)
H7 = Square(FileIndex.kH, RankIndex.k7)
H8 = Square(FileIndex.kH, RankIndex.k8)
