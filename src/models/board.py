from src.models.squares import *
from src.others.piece_factory import *


# This class handles all the Board related tasks
class Board:
    EmptyPiece = EmptyPiece()

    # Initialize an EMPTY board
    def __init__(self):
        # Initialize piece list with NIL pieces
        self.grid = [[None for _ in range(kNumberOfSquaresAlongY)] for _ in range(kNumberOfSquaresAlongX)]

        # A STACK for storing MOVESTATES - So we can UNDO them (helps in AI MOVES)
        self.moveStateStack = []

        # Fill the board with EMPTY pieces (piece type EMPTY)
        self.setupEmptyBoard()

        # If the piece moved is pawn
        # Store it in moved pawn property
        self.movedPawn = None
        # Indicates which rook was castled
        self.castledRook = None

    # MOVE PIECE from STARTING SQUARE to ENDING SQUARE
    def movePiece(self, piece, toSquare, player=None):
        previousPosition = piece.position
        # Check if PIECE can be put on the DESTINATION SQUARE
        if self.putPieceOnPosition(piece, toSquare, player):
            # Check if an EMPTY piece can be PUT on STARTING POSITION
            return self.putEmptyPieceOnPosition(previousPosition)

        return False

    # CHECK if given SQUARE is EMPTY
    def checkIfSquareIsEmpty(self, square):
        result = False

        # Check for an EMPTY piece
        if self.grid[square.rank][square.file] == EmptyPiece:
            result = True

        return result

    # CHECK if given SQUARE is not OUT OF BOUNDS
    def checkIfSquareIsNotNil(self, square):
        result = False

        try:
            piece = self.grid[square.rank][square.file]
            # Check for a NIL or out of bounds piece
            if piece:
                result = True
        except IndexError:
            result = False

        return result

    # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
    def checkIfEmptyOrEnemyPieceExists(self, color, square):
        result = False

        # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
        piece = self.grid[square.rank][square.file]
        if piece:
            result = piece == EmptyPiece or not (piece.color == color)

        return result

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

    # GET a PIECE from the given SQUARE
    def getPieceOnPosition(self, square):
        # Can not GET a piece from out of bounds
        piece = self.grid[square.rank][square.file]
        if not (piece == EmptyPiece or piece == None):
            return piece
        return None

    # PUT a given PIECE on the given SQUARE
    def putPieceOnPosition(self, piece, square, player=None):
        result = False
        # Can not go out of bounds
        try:
            existingPiece = self.grid[square.rank][square.file]
        except IndexError:
            existingPiece = None
        if existingPiece:
            if not (piece == EmptyPiece):
                existingPiece.captured = True
                self.grid[square.rank][square.file] = piece
                if player and not (existingPiece == EmptyPiece) and existingPiece in player.opponent.piecesList:
                    # Remove existing piece from pieces list (all occurences)
                    player.opponent.piecesList = Utility.removeAllOccurencesFromList(player.opponent.piecesList,
                                                                                     existingPiece)
                result = True
        return result

    # UNDO the TOP MOVE in MOVESTATESTACK
    def undoMove(self):
        moveState = self.moveStateStack.pop()
        # PUT the PIECES back where they were BEFORE the MOVE
        self.putPieceOnPosition(moveState.fromPieceState.piece, moveState.fromPieceState.position)
        self.putPieceOnPosition(moveState.toPieceState.piece, moveState.toPieceState.position)

        # RESET HASMOVED flag of BOTH the PIECES
        moveState.fromPieceState.piece.hasMoved = moveState.fromPieceState.hasMoved
        moveState.toPieceState.piece.hasMoved = moveState.toPieceState.hasMoved

        # RESET CAPTURED flag of BOTH the PIECES
        moveState.fromPieceState.piece.captured = False
        moveState.toPieceState.piece.captured = False

    # PUT an EMPTY PIECE on the given SQUARE
    def putEmptyPieceOnPosition(self, square):
        result = False
        # Check if SQUARE is not OUT OF BOUNDS
        piece = self.grid[square.rank][square.file]
        if piece:
            self.grid[square.rank][square.file] = EmptyPiece
            result = True

        return result

    # Fill the board with EMPTY pieces (piece type EMPTY)
    def setupEmptyBoard(self):
        for rank in allPiecesRankEnumeration:
            for file in allPiecesFileEnumeration:
                self.grid[rank][file] = EmptyPiece

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
                piece = PieceFactory.getPiece(piecesConfigurationList[rank][file], Square(file, rank))

                self.grid[rank][file] = piece

                # Add this PIECE to the LIST of PIECES
                piecesList.append(piece)

        # Return the LIST of PIECES to the corresponding PLAYER
        return piecesList

    def printBoard(self):
        for x in range(len(self.grid) - 1, -1, -1):
            for y in range(len(self.grid[0])):
                piece = self.grid[x][y]
                if piece:
                    if not (piece == EmptyPiece):
                        print(piece.symbol, sep="", end="")
                    else:
                        print(".", sep="", end="")
            print("\n")
