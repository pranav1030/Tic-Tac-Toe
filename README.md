# Tic-Tac-Toe

A simple program which pretends to play tic-tac-toe with the user. The computer plays the game using 'X's. The user plays the game using 'O's.

->the first move belongs to the computer - it always puts its first 'X' in the middle of the board;

->all the squares are numbered row by row starting with 1
the user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
the program checks if the game is over - there are four possible verdicts: the game should continue, or the game ends with a tie, your win, or the computer's win;

->the computer responds with its move and the check is repeated;

Requirements

Implement the following features:

->the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:

board[row][column]

->each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)


