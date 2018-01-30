from Constants import *
from Structures import *

# Here are all the constants
kMaxPlies = 2

kNumberOfSquaresAlongX = 12
kNumberOfSquaresAlongY = 12

class Symbols:
    newLine = "\n"
    nil     = "X"
    empty   = "-"
    pawn    = "P"
    knight  = "N"
    bishop  = "B"
    rook    = "R"
    queen   = "Q"
    king    = "K"

class Values:
    nil    = -1
    empty  = 0
    pawn   = 100
    knight = 300
    bishop = 305
    rook   = 500
    queen  = 900
    king   = 2000

X = Values.nil
i = Values.empty
P = -Values.pawn
N = -Values.knight
B = -Values.bishop
R = -Values.rook
Q = -Values.queen
K = -Values.king

p = -P
n = -N
b = -B
r = -R
q = -Q
k = -K

piecesConfigurationList = [
    
    [ X, X,   X, X, X, X, X, X, X, X,   X, X ],
    [ X, X,   X, X, X, X, X, X, X, X,   X, X ],
    
    [ X, X,   r, n, b, q, k, b, n, r,   X, X ],
    [ X, X,   p, p, p, p, p, p, p, p,   X, X ],
    [ X, X,   i, i, i, i, i, i, i, i,   X, X ],
    [ X, X,   i, i, i, i, i, i, i, i,   X, X ],
    [ X, X,   i, i, i, i, i, i, i, i,   X, X ],
    [ X, X,   i, i, i, i, i, i, i, i,   X, X ],
    [ X, X,   P, P, P, P, P, P, P, P,   X, X ],
    [ X, X,   R, N, B, Q, K, B, N, R,   X, X ],
    
    [ X, X,   X, X, X, X, X, X, X, X,   X, X ],
    [ X, X,   X, X, X, X, X, X, X, X,   X, X ]
]
