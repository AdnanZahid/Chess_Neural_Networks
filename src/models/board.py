from src.models.squares import *
from src.others.piece_factory import *


# This class handles all the Board related tasks
class Board:

    # Initialize an EMPTY board
    def __init__(self):
        # Simply set up an empty board
        self.setupEmptyBoard()

    # Fill the board with EMPTY pieces (piece type EMPTY)
    def setupEmptyBoard(self):
        # Initialize piece list with None pieces
        self.grid = [[EmptyPiece for _ in range(kNumberOfSquaresAlongFile)] for _ in range(kNumberOfSquaresAlongRank)]
        # Indicates if the last moved piece was a pawn
        self.movedPawn = None
        # Indicates which rook was castled
        self.castledRook = None

    # MOVE PIECE from STARTING SQUARE to ENDING SQUARE
    def movePiece(self, piece, toSquare, player=None):
        # Check if PIECE can be put on the DESTINATION SQUARE
        # And check if an EMPTY piece can be PUT on STARTING POSITION
        self.putEmptyPieceOnPosition(piece.position)
        return self.putPieceOnPosition(piece, toSquare, player)

    # CHECK if given SQUARE is EMPTY
    def checkIfSquareIsEmpty(self, square):
        return Utility.isEmptyPiece(self.getPieceOnPosition(square))

    # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
    def checkIfEmptyOrEnemyPieceExists(self, color, square):
        # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
        piece = self.getPieceOnPosition(square)
        return piece and (self.checkIfSquareIsEmpty(square) or not (piece.color == color))

    # CHECK for CLEAR PATH for a MOVE
    def checkForClearPath(self, move):
        result = True
        # GET a FILE RANK PAIR from a given MOVE - FILE RANK PAIR indicates the DIRECTION
        fileRankPair = Utility.getFileAndRankAdvance(EvaluationMove(move.fromSquare, move.toSquare))
        # GET the STARTING POSITION
        positionToCheck = move.fromSquare
        # GET the POSITION BEFORE the ENDING POSITION - Call it SECOND LAST SQUARE
        secondLastSquare = move.toSquare - Utility.getFileAndRankSingleAdvance(fileRankPair)
        # CHECK IF STARTING POSITION and SECOND LAST SQUARE are not the SAME - In other words, CHECK if we have to CHECK for a CLEAR PATH
        while not (positionToCheck == secondLastSquare):
            # INCREMENT the CURRENT POSITION STEP by STEP towards the FINAL POSITION
            positionToCheck = positionToCheck + Utility.getFileAndRankSingleAdvance(fileRankPair)
            # CHECK IF the CURRENT POSITION is EMPTY - Hence FIND OUT if a CLEAR PATH exists
            result = self.checkIfSquareIsEmpty(positionToCheck)
            # IF there is an OBSTACLE in BETWEEN, then do NOT CHECK other SQUARES
            if result == False:
                break
        return result

    # GET a PIECE from the given SQUARE (may be a valid piece or empty space)
    def getPieceOnPosition(self, square):
        if square.rank < RankIndex.k1 \
                or square.file < FileIndex.kA \
                or square.rank > RankIndex.k8 \
                or square.file > FileIndex.kH:
            return None
        # Will either return:
        # 1. A valid piece
        # 2. A empty space
        return self.grid[square.rank][square.file]

    # PUT a given PIECE on the given SQUARE
    def putPieceOnPosition(self, piece, square, player=None):
        result = False
        # Can not go out of bounds
        existingPiece = self.getPieceOnPosition(square)
        if existingPiece and Utility.isValidPiece(piece):
            self.grid[square.rank][square.file] = piece
            if player and Utility.isValidPiece(existingPiece) and existingPiece in player.opponent.piecesList:
                # Remove existing piece from pieces list (all occurences)
                player.opponent.piecesList = Utility.removeAllOccurencesFromList(player.opponent.piecesList,
                                                                                 existingPiece)
            result = True
        return result

    def putEmptyPieceOnPosition(self, square):
        self.grid[square.rank][square.file] = EmptyPiece

    # Fill the board with PIECES of the given COLOR
    def setupPieceBoard(self, color):
        # Set up a LIST of PIECES to be passed to the corresponding PLAYER
        piecesList = []
        if color == Color.white:
            # Pick WHITE RANK ENUMERATION if the given COLOR is WHITE
            pieceRankEnumeration = whitePiecesRankEnumeration
        else:
            # Pick BLACK RANK ENUMERATION if the given COLOR is BLACK
            pieceRankEnumeration = blackPiecesRankEnumeration
        # Enumerate over the RANK area occupied by the pieces of given COLOR
        for rank in pieceRankEnumeration:
            # Enumerate over all the FILES
            for file in allPiecesFileEnumeration:
                # Get values from a PRE-CONFIGURED ARRAY - DEFAULT CHESS STARTING CONFIGURATION
                square = Square(file, rank)
                piece = PieceFactory.getPiece(piecesConfigurationList[rank][file], square)
                self.putPieceOnPosition(piece, square)
                # Add this PIECE to the LIST of PIECES
                piecesList.append(piece)
        # Return the LIST of PIECES to the corresponding PLAYER
        return piecesList

    def toString(self):
        string = ""
        for rank in range(kNumberOfSquaresAlongRank):
            for file in range(kNumberOfSquaresAlongFile):
                piece = self.getPieceOnPosition(Square(file, rank))
                if piece:
                    if Utility.isValidPiece(piece):
                        string += piece.symbol
                    else:
                        string += Symbols.empty
            string += Symbols.newLine

        return string

    def __repr__(self):
        string = ""
        for rank in reversed(range(kNumberOfSquaresAlongRank)):
            for file in range(kNumberOfSquaresAlongFile):
                piece = self.getPieceOnPosition(Square(file, rank))
                if piece:
                    if Utility.isValidPiece(piece):
                        string += piece.symbol
                    else:
                        string += Symbols.empty
            string += Symbols.newLine

        return string
