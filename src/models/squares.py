# This class represents a square and its essential functions
class Square:
    def __init__(self,file,rank):
        self.file = file
        self.rank = rank
        self.order = (self.rank * 8) + self.file
        
    def __eq__(self,other):
        return self.file == other.file\
            and self.rank == other.rank

    def __ne__(self,other):
        return ~(self == other)

    def __add__(square,fileRankPair):
        return Square(square.file + fileRankPair[0],square.rank + fileRankPair[1])

    def __sub__(square,fileRankPair):
        return Square(square.file - fileRankPair[0],square.rank - fileRankPair[1])

    def __lt__(self,other):
            return self.order < other.order