import re

from src.others.piece_factory import *


# This class helps with FEN related logic
class FENHelper:

    def __init__(self, delegate):
        self.delegate = delegate

    def setFEN(self, fenString):

        # Separate all FEN strings for each corresponding domain
        fenStringsArray = fenString.split(" ")

        # Set board using FEN Board String
        piecesSymbolsString = fenStringsArray[0]
        self.setBoardUsingFEN(piecesSymbolsString)

        # Parse the color of the player to move next
        if fenStringsArray[1] == "w":
            self.delegate.currentPlayer = self.delegate.whitePlayer
        elif fenStringsArray[1] == "b":
            self.delegate.currentPlayer = self.delegate.blackPlayer

        # Set the castling rights
        castlingSymbolsString = fenStringsArray[2]
        self.setCastlingRightsUsingFEN(castlingSymbolsString)

        # Set the last enpassant pawn
        enpassantString = fenStringsArray[3]
        self.delegate.board.movedPawn = self.getMovedPawnUsingFEN(enpassantString)

        # Set the half move clock and full move number
        self.delegate.halfMoveClock = int(fenStringsArray[4])
        self.delegate.fullMoveNumber = int(fenStringsArray[5])

    def getFEN(self):
        fenString = ""

        # Pieces FEN
        for rank in reversed(range(kNumberOfSquaresAlongRank)):
            fenFileString = ""
            fileEmptyPieceCount = 0
            for file in range(kNumberOfSquaresAlongFile):
                piece = self.delegate.board.getPieceOnPosition(Square(file, rank))
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
        if self.delegate.currentPlayer.color == Color.white:
            fenString += " w "
        else:
            fenString += " b "

        # Castling FEN
        # White castling
        if self.delegate.whitePlayer.hasKingSideCastlingRights():
            fenString += FENSymbols.white_king
        if self.delegate.whitePlayer.hasQueenSideCastlingRights():
            fenString += FENSymbols.white_queen

        # Black castling
        if self.delegate.blackPlayer.hasKingSideCastlingRights():
            fenString += FENSymbols.black_king
        if self.delegate.blackPlayer.hasQueenSideCastlingRights():
            fenString += FENSymbols.black_queen

        # Enpassant pawn
        if self.delegate.board.movedPawn:
            fenString += " " + str(self.delegate.board.movedPawn.position)
        else:
            fenString += " -"

        # Half move clock
        fenString += " 0"

        # Full move counter
        fenString += " 1"
        return fenString

    def setBoardUsingFEN(self, piecesSymbolsString):
        # Empty the board (to make room for new pieces)
        self.delegate.board.setupEmptyBoard()

        rank, file = 7, 0
        # Set each invidual piece character by character from the string
        for fenSymbol in piecesSymbolsString:
            if re.match("[rbqkpn]", fenSymbol):
                color = Color.black

                position = Square(file, rank)
                piece = PieceFactory.getPiece(-symbolsToValueDictionary[fenSymbol.upper()], position)
                piece.color = color
                self.delegate.board.putPieceOnPosition(piece, position)

                file += 1

                if piece.value == Values.pawn:
                    if rank == RankIndex.k7:
                        piece.hasMoved = False
                    else:
                        piece.hasMoved = True

            elif re.match("[RBQKPN]", fenSymbol):
                color = Color.white

                position = Square(file, rank)
                piece = PieceFactory.getPiece(symbolsToValueDictionary[fenSymbol.upper()], position)
                piece.color = color
                self.delegate.board.putPieceOnPosition(piece, position)

                file += 1

                if piece.value == Values.pawn:
                    if rank == RankIndex.k2:
                        piece.hasMoved = False
                    else:
                        piece.hasMoved = True

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
                self.delegate.whitePlayer.setKingSideCastlingRights(True)
            elif castlingSymbol == "Q":
                self.delegate.whitePlayer.setQueenSideCastlingRights(True)
            elif castlingSymbol == "k":
                self.delegate.blackPlayer.setKingSideCastlingRights(True)
            elif castlingSymbol == "q":
                self.delegate.blackPlayer.setQueenSideCastlingRights(True)

    def getMovedPawnUsingFEN(self, enpassantString):
        if enpassantString == "-" or len(enpassantString) < 2:
            return None

        enpassantSquare = Square(enpassantString[0], enpassantString[1])
        if self.delegate.currentPlayer == self.delegate.whitePlayer:
            movedPawn = self.delegate.board.getPieceOnPosition(
                Square(enpassantSquare.file, enpassantSquare.rank - 1))
        else:
            movedPawn = self.delegate.board.getPieceOnPosition(
                Square(enpassantSquare.file, enpassantSquare.rank + 1))

        return movedPawn

    def setCastlingRightsToFalse(self):
        self.delegate.whitePlayer.setKingSideCastlingRights(False)
        self.delegate.whitePlayer.setQueenSideCastlingRights(False)
        self.delegate.blackPlayer.setKingSideCastlingRights(False)
        self.delegate.blackPlayer.setQueenSideCastlingRights(False)
