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

        # Separate all FEN strings for each corresponding domain
        fenStringsArray = fenString.split(" ")

        # Set board using FEN Board String
        piecesSymbolsString = fenStringsArray[0]
        self.setBoardUsingFEN(piecesSymbolsString)

        # Parse the color of the player to move next
        if fenStringsArray[1] == "w":
            self.currentPlayer = self.whitePlayer
        elif fenStringsArray[1] == "b":
            self.currentPlayer = self.blackPlayer
        else:
            print("Color of the player to move next incorrect.")

        # Set the castling rights
        castlingSymbolsString = fenStringsArray[2]
        self.setCastlingRightsUsingFEN(castlingSymbolsString)

        # Set the last enpassant pawn
        enpassantString = fenStringsArray[3]
        self.board.movedPawn = self.getMovedPawnUsingFEN(enpassantString)

        # Set the half move clock and full move number
        if len(fenStringsArray) == 6:
            try:
                self.halfMoveClock = int(fenStringsArray[4])
                self.fullMoveNumber = int(fenStringsArray[5])
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

    def setBoardUsingFEN(self, piecesSymbolsString):
        # Empty the board (to make room for new pieces)
        self.board.setupEmptyBoard()

        rank, file = 7, 0
        # Set each invidual piece character by character from the string
        for fenSymbol in piecesSymbolsString:
            if re.match("[rbqkpn]", fenSymbol):
                color = Color.black

                position = Square(file, rank)
                piece = PieceFactory.getPiece(-symbolsToValueDictionary[fenSymbol.upper()], position)
                piece.color = color
                self.board.putPieceOnPosition(piece, position)

                file += 1

            elif re.match("[RBQKPN]", fenSymbol):
                color = Color.white

                position = Square(file, rank)
                piece = PieceFactory.getPiece(symbolsToValueDictionary[fenSymbol.upper()], position)
                piece.color = color
                self.board.putPieceOnPosition(piece, position)

                file += 1

            elif fenSymbol in '12345678':

                file += int(fenSymbol)

            elif fenSymbol == '/':
                file = 0
                rank -= 1

    def setCastlingRightsUsingFEN(self, castlingSymbolsString):
        self.setCastlingRightsToFalse()
        # Set each invidual castling right character by character from the string
        # By setting rook's hasMoved property
        for castlingSymbol in castlingSymbolsString:
            if castlingSymbol == "K":
                self.whitePlayer.setKingSideCastlingRights(True)
            elif castlingSymbol == "Q":
                self.whitePlayer.setQueenSideCastlingRights(True)
            elif castlingSymbol == "k":
                self.blackPlayer.setKingSideCastlingRights(True)
            elif castlingSymbol == "q":
                self.blackPlayer.setQueenSideCastlingRights(True)

    def getMovedPawnUsingFEN(self, enpassantString):
        if enpassantString == "-" or len(enpassantString) < 2:
            return None

        enpassantSquare = Square(enpassantString[0], enpassantString[1])
        if self.currentPlayer == self.whitePlayer:
            movedPawn = self.board.getPieceOnPosition(
                Square(enpassantSquare.file, enpassantSquare.rank - 1))
        else:
            movedPawn = self.board.getPieceOnPosition(
                Square(enpassantSquare.file, enpassantSquare.rank + 1))

        return movedPawn

    def setCastlingRightsToFalse(self):
        self.whitePlayer.setKingSideCastlingRights(False)
        self.whitePlayer.setQueenSideCastlingRights(False)
        self.blackPlayer.setKingSideCastlingRights(False)
        self.blackPlayer.setQueenSideCastlingRights(False)
