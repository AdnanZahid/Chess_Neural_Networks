import re

from src.models.ai_player import *
from src.models.board import *
from src.others.structures import *


# This class represents all the game logic in general
class GameLogic:

    def __init__(self, isWhitePlayerAI=False, isBlackPlayerAI=False):
        self.board = Board()

        if isWhitePlayerAI:
            self.whitePlayer = AIPlayer(Color.white, self.board)
        else:
            self.whitePlayer = Player(Color.white, self.board)

        if isBlackPlayerAI:
            self.blackPlayer = AIPlayer(Color.black, self.board)
        else:
            self.blackPlayer = Player(Color.black, self.board)

        self.whitePlayer.opponent = self.blackPlayer
        self.blackPlayer.opponent = self.whitePlayer

        self.currentPlayer = self.whitePlayer

    def move(self, move):
        if self.currentPlayer.move(move):
            self.changeTurn()
            return True
        return False

    def changeTurn(self):
        self.currentPlayer = self.currentPlayer.opponent

    def isAITurn(self):
        return self.currentPlayer.isAI

    def input(self):
        self.inputHandlerDelegate.didTakeInput(self.currentPlayer.generateMove())

    def setFEN(self, fenString):
        # Empty the board (to make room for new pieces)
        self.board.setupEmptyBoard()
        # Split the FEN with whitespaces
        fenArray = fenString.split(" ")
        # There are 4 sections in FEN
        if len(fenArray) < kSectionsInFEN:
            print("Number of argument incorrect in the FEN.")

        # Parse the board description
        fenPiecesArray = fenArray[0].split("/")
        if not (len(fenPiecesArray) == kNumberOfSquaresAlongRank):
            print("Board representation incorrect in the FEN.")

        for rank, fenFileString in enumerate(fenPiecesArray):
            fileEmptyPieceCount = 0
            for file, fenSymbol in enumerate(fenFileString):
                if re.match("[rbqkpn]", fenSymbol):
                    color = Color.black

                    position = Square(file, rank)
                    self.board.putPieceOnPosition(
                        PieceFactory.getPiece(symbolsToValueDictionary[fenSymbol.upper()], position), position)

                elif re.match("[RBQKPN]", fenSymbol):
                    color = Color.white

                    position = Square(file, rank)
                    self.board.putPieceOnPosition(
                        PieceFactory.getPiece(symbolsToValueDictionary[fenSymbol.upper()], position), position)
                else:
                    try:
                        fileEmptyPieceCount += int(fenSymbol)

                        for fileEmptyPiece in range(fileEmptyPieceCount):
                            file = fileEmptyPiece
                            self.board.putEmptyPieceOnPosition(Square(fileEmptyPiece, rank))
                    except:
                        print("Board representation incorrect in the FEN.")

                # Parse the color of the player to move next
                if fenArray[1] == "w":
                    self.currentPlayer = self.whitePlayer
                elif fenArray[1] == "b":
                    self.currentPlayer = self.blackPlayer
                else:
                    print("Color of the player to move next incorrect.")

                # Parse the castling, en passant, half moves and full moves number
                castling = fenArray[2]
                enpassant = fenArray[3]
                if len(fenArray) == 6:
                    try:
                        halfMoves = int(fenArray[4])
                        fullMoves = int(fenArray[5])
                    except:
                        print("Impossible to have the number of full move or half move.")

    def getFEN(self):
        fenString = ""

        # Pieces FEN
        for rank in reversed(range(kNumberOfSquaresAlongRank)):
            fenFileString = ""
            fileEmptyPieceCount = 0
            for file in range(kNumberOfSquaresAlongFile):
                piece = self.board.getPieceOnPosition(Square(file, rank))
                if Utility.isValidPiece(piece):
                    if fileEmptyPieceCount == 0:
                        fenFileString += piece.fenSymbol
                    else:
                        fenFileString += str(fileEmptyPieceCount) + piece.fenSymbol
                else:
                    fileEmptyPieceCount += 1
            if not (fileEmptyPieceCount == 0):
                fenFileString += str(fileEmptyPieceCount)

            if not (rank == RankIndex.k8):
                fenString += "/"
            fenString += fenFileString

        # Side to move FEN
        if self.currentPlayer.color == Color.white:
            fenString += " w "
        else:
            fenString += " b "

        # Castling FEN
        # White castling
        if self.whitePlayer.hasKingSideCastlingRights():
            fenString += FENSymbols.white_king
        if self.whitePlayer.hasQueenSideCastlingRights():
            fenString += FENSymbols.white_queen

        # Black castling
        if self.blackPlayer.hasKingSideCastlingRights():
            fenString += FENSymbols.black_king
        if self.blackPlayer.hasQueenSideCastlingRights():
            fenString += FENSymbols.black_queen

        # Enpassant pawn
        if self.board.movedPawn:
            fenString += " " + str(self.board.movedPawn.position)
        else:
            fenString += " -"

        # Half move clock
        fenString += " 0"

        # Full move counter
        fenString += " 1"
        return fenString
