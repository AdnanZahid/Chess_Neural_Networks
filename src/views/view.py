import os
from pygame import *

from src.others.move_generator import *

# Constants
square_size = 125
columns, rows = kNumberOfSquaresAlongFile, kNumberOfSquaresAlongRank
screen_size = (columns * square_size, rows * square_size)
white_color = (236, 218, 185)
black_color = (175, 137, 104)
green_color = (0, 255, 0)


# This class handles all the view related activity
class View:

    def __init__(self):
        self.gameOver = False

    def runGame(self, gameLogic):
        board = gameLogic.board
        self.resetMoveState()
        while not (self.isGameOver()):
            player = gameLogic.currentPlayer
            # Initialization
            init()
            screen = display.set_mode(screen_size)

            # Events
            for e in event.get():
                if e.type == QUIT:
                    pass
                elif e.type == MOUSEBUTTONUP:
                    position = mouse.get_pos()
                    file, rank = self.convertCoordinatesForModel(position[0], position[1])

                    if not self.possibleMoves:
                        self.selectedPiece = board.getPieceOnPosition(Square(file, rank))
                        self.possibleMoves = MoveGenerator.generatePossibleTargetSquaresForFileAndRank(file, rank,
                                                                                                       board, player)

                    elif Utility.isValidPiece(self.selectedPiece):
                        self.move(EvaluationMove(self.selectedPiece.position, Square(file, rank)))

            # Drawing
            screen.fill(white_color)
            self.draw(screen, board)
            display.flip()

            # Clock ticking
            time.Clock().tick(60)

        self.inputHandlerDelegate.setupNewGame()

    def output(self):
        # Reset state once output is done
        self.resetMoveState()

    def move(self, move):
        self.inputHandlerDelegate.didTakeInput(move)
        # Reset state once move is done
        self.resetMoveState()

    def cancelMove(self):
        # Reset state once move is cancelled
        self.resetMoveState()

    def resetMoveState(self):
        self.selectedPiece = EmptyPiece
        self.possibleMoves = []

    def draw(self, screen, board):
        self.drawSquares(screen)
        self.drawPieces(screen, board)
        self.drawPossibleTargetSquares(screen)

    def drawSquares(self, screen):
        for file in range(columns):
            for rank in range(rows):
                if (file + rank) % 2:
                    color = white_color
                else:
                    color = black_color
                draw.rect(screen, color, Rect(file * square_size, rank * square_size, square_size, square_size))

    def drawPieces(self, screen, board):
        for file in range(kNumberOfSquaresAlongFile):
            for rank in range(kNumberOfSquaresAlongRank):
                piece = board.getPieceOnPosition(Square(file, rank))
                if Utility.isValidPiece(piece):
                    x, y = self.convertCoordinatesForGUI(file, rank)
                    path = os.path.dirname(__file__) + "/images/" + piece.symbol + ".png"
                    sprite = image.load(path)
                    sprite = transform.scale(sprite, (square_size, square_size))
                    screen.blit(sprite, Rect(x, y, square_size, square_size))

    def drawPossibleTargetSquares(self, screen):
        for square in self.possibleMoves:
            x, y = self.convertCoordinatesForGUI(square.file, square.rank)
            surface = Surface((square_size, square_size))
            surface.set_alpha(100)
            surface.fill(green_color)
            screen.blit(surface, (x, y))

    def convertCoordinatesForGUI(self, file, rank):
        # Transform according to our view
        # Transform = rows - 1, because view is inverted
        # Multiplier = square_size, because each square needs to be a certain distance apart
        x = file * square_size
        y = (rows - 1 - rank) * square_size
        return x, y

    def convertCoordinatesForModel(self, x, y):
        # Transform according to our view
        # Transform = rows - 1, because view is inverted
        # Divider = square_size, because each square is a certain distance apart in GUI but adjacent in model
        file = x // square_size
        rank = rows - 1 - (y // square_size)
        return file, rank

    def isGameOver(self):
        return self.gameOver

    def setIsGameOver(self, gameOver):
        self.gameOver = gameOver
