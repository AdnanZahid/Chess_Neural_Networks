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

        fenStringsArray = fenString.split(" ")
        boardString = fenStringsArray[0]

        # Empty the board (to make room for new pieces)
        self.board.setupEmptyBoard()

        rank, file = 0, 0
        for fenSymbol in boardString:
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
                rank += 1

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
