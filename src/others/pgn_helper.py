import chess.pgn

from paths import *
from src.models.squares import *


# This class helps with PGN related logic
class PGNHelper:

    def __init__(self, delegate):
        self.delegate = delegate

    def setPGN(self, pgnFileName):
        pgn = open(DATA_DIR + "/" + pgnFileName)
        game = chess.pgn.read_game(pgn)

        for move in game.main_line():
            self.delegate.move(
                EvaluationMove(Square.initializeFromOrder(move.from_square),
                               Square.initializeFromOrder(move.to_square)))
