# This class manages mobility and list of moves for a piece
class MoveStrategy:

    def __init__(self, piece, color, directionsList, board):
        self.piece = piece
        self.color = color
        self.directionsList = directionsList
        self.board = board

    def getMobility(self, position):
        return len(self.generateAllMoves(position))

    def generateAllMoves(self):

        possibleMovesToSquaresList = []

        delegate = self.piece.delegate
        self.piece.delegate = None

        if self.color == self.board.currentTurnColor:
            for direction in self.directionsList:
                possibleMovesToSquaresList.extend(self.generateMove(self.piece.position, direction))

        self.piece.delegate = delegate

        return set(possibleMovesToSquaresList)
