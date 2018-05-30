# Chess Neural Networks

**Overview:**

This is a simple python implementation of a Chess game which encompasses the following features:

1. Legal moves validation
2. AI player which uses minimax based tree search to find optimal moves at any given position
3. FEN and PGN parsers to set custom positions

**How to run:**

To run the game, simply run ```python3 -m main```

To run the unit tests, run ```python3 -m tests.main```

**Screenshot:**

![Screenshot](https://github.com/AdnanZahid/Chess_Neural_Networks/blob/master/screenshot.png)

**Basic structure:**

This project implements an MVC architecture:

**Models:**

1. ```game_logic.py``` contains game centric information such as players, turn to move and FEN/PGN helpers

2. ```player.py``` contains player centric information such as color, pieces list, castling information, check and checkmate logic

3. ```ai_player.py``` contains a sub-class of Player and it contains AI tree searching logic

4. ```board.py``` contains board centric information and all the necessary steps to set a valid piece or empty piece at certain squares

5. ```square.py``` contains square centric information such as file, rank, order, addition, subtraction and equality of squares

6. ```piece.py``` contains piece centric information such as position, color, sliding or jumping pieces, directions list and whether the piece can move to the desired position or not

7. ```bishop.py```, ```king.py```, ```knight.py```, ```pawn.py```, ```queen.py``` and ```rook.py``` all contain sub-classes of Piece

**Controller:**

The controller simply defines game logic, which players are AI or human, the view and whether to take input from view (human move) or from models (AI move).

**View:**

This simply presents the board in human viewable form. It draws images corresponding to pieces on the board, highlights possible moves in green color, allows the player to pick pieces up and make moves or cancel the desired move.

**Others:**

1. ```constants.py``` defines the constants such as number of plies, number of squares across ranks and files, piece symbols, piece values and piece configuration on the board

2. ```error_handler.py``` defines all the possible errors and shows them in a human readable format

3. ```evaluation_handler.py``` defines the evaluation function based on certain parameters such as piece values and mobility

4. ```fen_helper.py``` parses FEN strings into piece models and places them on the board

5. ```move_generator.py``` helps in generating all possible moves for pieces, verifying whether a piece can move to a certain position and actually make that move if the criteria is met

6. ```pgn_helper.py``` parses PGN strings into piece models and places them on the board

7. ```piece_factory.py``` simply constructs pieces based on simple factory pattern, it takes piece value and position as input and returns a piece of that type and puts it on the given position

8. ```structures.py``` contains basic structures such as Move, EmptyPiece, PieceState, MoveState, FileIndex, RankIndex, Color, Strategy and MoveType

9. ``` utility.py``` contains all the basic file, rank and directional advance checks

**To do:**

1. A probability based tree search rather than a conventional minimax search (distance to root)

2. Deep learning for move ordering
3. Null move pruning
4. Forced moves based on clock
5. Asynchronous UI and searches

**Inspired by:**

```Giraffe: Using Deep Reinforcement Learning to Play Chess by Matthew Lai``` (https://arxiv.org/abs/1509.01549v2)

**For further help or contribution:**

Please feel free to contact me at:

Email: adnaan.zaahid@gmail.com

Phone: +92-314-2128544