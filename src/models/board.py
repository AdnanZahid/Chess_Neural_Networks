from src.models.pieces.piece_factory import *
from src.others.error_handler import *


# This class handles all the Board related tasks
class Board:
    EmptyPiece = EmptyPiece()

    # Initialize an EMPTY board
    def __init__(self):
        self.kNumberOfSquaresAlongX = piecesConfigurationList[0].count
        self.kNumberOfSquaresAlongY = piecesConfigurationList.count

        # Initialize piece list with Nil pieces
        self.grid = [[None for x in range(kNumberOfSquaresAlongY)] for y in range(kNumberOfSquaresAlongX)]

        # Assign the CURRENT TURN COLOR to WHITE by default - Later it changes according to turns
        self.currentTurnColor = Color.white

        # EVALUATION VALUE for computing AI MOVES - POSITIVE for WHITE domination and NEGATIVE for BLACK domination
        self.evaluationValue = 0

        # A STACK for storing MOVESTATES - So we can UNDO them (helps in AI MOVES)
        self.moveStateStack = []

        # Fill the board with EMPTY pieces (piece type EMPTY)
        self.setupEmptyBoard()

    # MOVE PIECE from STARTING SQUARE to ENDING SQUARE
    def movePiece(self, move, checkCurrentTurn):

        result = False
        piece = None

        # STARTING and ENDING squares are not the same
        if not (move.fromSquare == move.toSquare):

            # PIECE is not EMPTY or OUT OF BOUNDS
            piece = self.getPieceOnPosition(move.fromSquare)
            if not (piece == EmptyPiece or piece == None):

                # This PIECE COLOR has the CURRENT TURN
                if piece.color == self.currentTurnColor or checkCurrentTurn == False:

                    # Check if PIECE can MOVE
                    if piece.moveToSquare(move.toSquare):

                        # Check if PIECE can be put on the DESTINATION SQUARE
                        if self.putPieceOnPosition(piece, move.toSquare, True):
                            # Check if an EMPTY piece can be PUT on STARTING POSITION
                            result = self.putEmptyPieceOnPosition(move.fromSquare)
                    else:
                        ErrorHandler.logError(self, piece, move.toSquare, Error.invalidMove)
                else:
                    ErrorHandler.logError(self, piece, move.toSquare, Error.wrongTurn)
            else:
                ErrorHandler.logError(self, piece, move.toSquare, Error.invalidPiece)
        else:
            ErrorHandler.logError(self, piece, move.toSquare, Error.samePosition)

        return result

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
            if not (piece == None):
                result = True
        except IndexError:
            result = False

        return result

    # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
    def checkIfEmptyOrEnemyPieceExists(self, color, square):

        result = False

        # CHECK if given SQUARE is EMPTY or occupied by the ENEMY
        piece = self.grid[square.rank][square.file]
        if not (piece == None):
            result = piece == EmptyPiece or not (piece.color == color)

        return result

    # CHECK for CLEAR PATH for a MOVE
    def checkForClearPath(self, move):

        result = True

        # GET a FILE RANK PAIR from a given MOVE - FILE RANK PAIR indicates the DIRECTION
        fileRankPair = getFileAndRankAdvance(EvaluationMove(move.fromSquare, move.toSquare))

        # GET the STARTING POSITION
        positionToCheck = move.fromSquare

        # GET the POSITION BEFORE the ENDING POSITION - Call it SECOND LAST SQUARE
        secondLastSquare = move.toSquare - getFileAndRankSingleAdvance(fileRankPair)

        # CHECK IF STARTING POSITION and SECOND LAST SQUARE are not the SAME - In other words, CHECK if we have to CHECK for a CLEAR PATH
        while not (positionToCheck == secondLastSquare):

            # INCREMENT the CURRENT POSITION STEP by STEP towards the FINAL POSITION
            positionToCheck = positionToCheck + getFileAndRankSingleAdvance(fileRankPair)

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
    def putPieceOnPosition(self, piece, square, pushToStack):

        result = False

        try:
            # Can not go out of bounds
            existingPiece = self.grid[square.rank][square.file]
        except IndexError:
            existingPiece = None

        if not (existingPiece == None):

            # King can not be captured
            if existingPiece == EmptyPiece or not (existingPiece.value == abs(Values.king)):

                # Destination square is empty
                # And no friendly fire
                if existingPiece == EmptyPiece \
                        or not (existingPiece.color == piece.color):

                    if not (piece == EmptyPiece):
                        existingPiece.captured = True

                    self.grid[square.rank][square.file] = piece

                    if pushToStack:
                        # Storing the MOVESTATE in a stack - So we can UNDO them (helps in AI MOVES)
                        self.moveStateStack.append(MoveState( \
                            # FROM PIECE STATE
                            PieceState(piece, piece.position, piece.hasMoved),
                            # TO PIECE STATE
                            PieceState(existingPiece, square, piece.hasMoved)))

                    result = True
                    piece.updatePosition(square, pushToStack)
                else:
                    ErrorHandler.logError(self, piece, square, Error.friendlyFire)
            else:
                ErrorHandler.logError(self, piece, square, Error.kingCapture)
        else:
            ErrorHandler.logError(self, piece, square, Error.invalidDestination)

        return result

    # UNDO the TOP MOVE in MOVESTATESTACK (helps in AI MOVES)
    def undoMove(self):
        moveState = moveStateStack.pop()

        # PUT the PIECES back where they were BEFORE the MOVE
        self.putPieceOnPosition(moveState.fromPieceState.piece, moveState.fromPieceState.position, False)
        self.putPieceOnPosition(moveState.toPieceState.piece, moveState.toPieceState.position, False)

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
        if not (piece == None):
            self.grid[square.rank][square.file] = EmptyPiece
            result = True

        return result

    # Fill the board with EMPTY pieces (piece type EMPTY)
    def setupEmptyBoard(self):
        for rank in allPiecesRankEnumeration:
            for file in allPiecesFileEnumeration:
                self.grid[rank][file] = EmptyPiece

    # Fill the board with PIECES of the given COLOR
    def setupPieceBoard(self, color, pieceDelegate):

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
                piece = PieceFactory.getPiece(piecesConfigurationList[rank][file], Square(file, rank), pieceDelegate,
                                              self)

                self.grid[rank][file] = piece

                # Add this PIECE to the LIST of PIECES
                piecesList.append(piece)

        # Return the LIST of PIECES to the corresponding PLAYER
        return piecesList

    def printBoard(self):
        for x in range(len(self.grid) - 1, -1, -1):
            for y in range(len(self.grid[0])):
                piece = self.grid[x][y]
                if not (piece == None):
                    if not (piece == EmptyPiece):
                        print(piece.symbol, sep="", end="")
                    else:
                        print(".", sep="", end="")
            print("\n")
