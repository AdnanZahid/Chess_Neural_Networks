import sys

# Here are all the constants
kMaxPlies = 1

kNumberOfSquaresAlongFile = 8
kNumberOfSquaresAlongRank = 8

kMaxPossibleNumber = sys.maxsize
kMinPossibleNumber = -sys.maxsize - 1


class Symbols:
    newLine = "\n"
    empty = "·"
    white_pawn = "♙"
    white_knight = "♘"
    white_bishop = "♗"
    white_rook = "♖"
    white_queen = "♕"
    white_king = "♔"
    black_pawn = "♟"
    black_knight = "♞"
    black_bishop = "♝"
    black_rook = "♜"
    black_queen = "♛"
    black_king = "♚"


class FENSymbols:
    white_pawn = "P"
    white_knight = "N"
    white_bishop = "B"
    white_rook = "R"
    white_queen = "Q"
    white_king = "K"
    black_pawn = "p"
    black_knight = "n"
    black_bishop = "b"
    black_rook = "r"
    black_queen = "q"
    black_king = "k"


class Values:
    empty = 0
    pawn = 100
    knight = 300
    bishop = 305
    rook = 500
    queen = 900
    king = 2000


i = Values.empty
P = -Values.pawn
N = -Values.knight
B = -Values.bishop
R = -Values.rook
Q = -Values.queen
K = -Values.king

# This is done to represent the symbols bottom to top
# When in fact they are top to bottom (stored that way in the array)
p = -P
n = -N
b = -B
r = -R
q = -Q
k = -K

piecesConfigurationList = [

    [r, n, b, q, k, b, n, r],
    [p, p, p, p, p, p, p, p],
    [i, i, i, i, i, i, i, i],
    [i, i, i, i, i, i, i, i],
    [i, i, i, i, i, i, i, i],
    [i, i, i, i, i, i, i, i],
    [P, P, P, P, P, P, P, P],
    [R, N, B, Q, K, B, N, R]
]
