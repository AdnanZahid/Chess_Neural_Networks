import os
from pygame import *

from src.others.move_generator import *

# Constants
square_size = 100
columns, rows = 8, 8
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
        self.possibleMoves = []
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
                    x, y = self.convertCoordinatesForModel(position[0], position[1])

                    if not self.possibleMoves:
                        self.selectedPiece = board.grid[x][y]
                        self.possibleMoves = self.getPossibleMoves(x, y, board, player)

                    elif not (self.selectedPiece == EmptyPiece or self.selectedPiece == None):
                        self.move(EvaluationMove(self.selectedPiece.position, Square(y, x)))

            # Drawing
            screen.fill(white_color)
            self.draw(screen, board)
            display.flip()

            # Clock ticking
            time.Clock().tick(60)

        self.inputHandlerDelegate.setupNewGame()

    def output(self):
        # Nothing to do here since PyGame runs in a game loop architecture (instead of a turn based architecture)
        pass

    def move(self, move):
        self.inputHandlerDelegate.didTakeInput(move)
        self.selectedPiece = EmptyPiece
        self.possibleMoves = []

    def cancelMove(self):
        self.selectedPiece = EmptyPiece
        self.possibleMoves = []

    def draw(self, screen, board):
        self.drawSquares(screen)
        self.drawPieces(screen, board)
        self.drawPossibleMoves(screen)

    def drawSquares(self, screen):
        for x in range(columns):
            for y in range(rows):
                if (x + y) % 2:
                    draw.rect(screen, white_color, Rect(x * square_size, y * square_size, square_size, square_size))
                else:
                    draw.rect(screen, black_color, Rect(x * square_size, y * square_size, square_size, square_size))

    def drawPieces(self, screen, board):
        for x in range(len(board.grid)):
            for y in range(len(board.grid[0])):
                piece = board.grid[x][y]
                if not (piece == EmptyPiece or piece == None):
                    xPosition, yPosition = self.convertCoordinatesForGUI(x, y)
                    path = os.path.dirname(__file__) + "/images/" + piece.symbol + ".png"
                    sprite = image.load(path)
                    sprite = transform.scale(sprite, (square_size, square_size))
                    screen.blit(sprite, Rect(xPosition, yPosition, square_size, square_size))

    def getPossibleMoves(self, x, y, board, player):
        piece = board.grid[x][y]

        if not (piece == EmptyPiece or piece == None):
            return MoveGenerator.generatePossibleTargetSquares(piece, board, player)
        else:
            return []

    def drawPossibleMoves(self, screen):
        for square in self.possibleMoves:
            x, y = self.convertCoordinatesForGUI(square.rank, square.file)
            surface = Surface((square_size, square_size))
            surface.set_alpha(100)
            surface.fill(green_color)
            screen.blit(surface, (x, y))

    def convertCoordinatesForGUI(self, x, y):
        # Transform according to our view
        # Transform = +7, because view is inverted
        # Multiplier = square_size, because each square needs to be a certain distance apart
        xPosition = y * square_size
        yPosition = (7 - x) * square_size
        return xPosition, yPosition

    def convertCoordinatesForModel(self, x, y):
        # Transform according to our view
        # Transform = +7, because view is inverted
        # Divider = square_size, because each square is a certain distance apart in GUI but adjacent in model
        xPosition = 7 - y // square_size
        yPosition = x // square_size
        return xPosition, yPosition

    def isGameOver(self):
        return self.gameOver

    def setIsGameOver(self, gameOver):
        self.gameOver = gameOver
