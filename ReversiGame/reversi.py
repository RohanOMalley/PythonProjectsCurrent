###
### Author: Rohan O'Malley
### Course: Csc 110
### Description: Program plays a game of Reversi on a single row, takes
### the users input to play the game of Xs and Os until the whole board
### is covered. Then the result is printed at the bottom. Also, the game prints
### out on a canvas as the game is played.
###

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, turn, pos):

    '''This function takes the position given from the user
    and checks the board list to see if the board already has
    a spot there, if not there then function returns True'''

    if pos-1 < len(board) and pos-1 >= 0:
        if board[pos-1] == EMPTY:
            return True
    return False


def move(board, turn, pos):
    ''' this function takes the position and puts it on the board
    then checks to see if the turn of the player and checks the left of
    the currrent postion to see if it can flip any characters and it checks
    to the right of that current positon.'''
    index = pos - 1
    board[index] = turn
    opponent = get_opposite_turn(turn)
    if index < (len(board) - 1):
        # loops are used to check to the right to see if any characters can
        # be flipped
        i = index + 1
        while (i < (len(board) - 1)) and (board[i] == opponent):
            i += 1
        if board[i] == turn:
            while i != index:
                board[i] = turn
                i -= 1
    if index > 0:
        i = index - 1
        # loop is used to check if any characters to the left need to be flipped
        while (board[i] == opponent) and (i > 0):
            i -= 1
        if board[i] == turn:
            while i != index:
                board[i] = turn
                i += 1


def get_move(turn):

    '''Function uses the users input depending on if
   its white or blacks turn '''

    if turn == WHITE:
        white_input = int(input('O choose your move:\n'))
        return white_input
    elif turn == BLACK:
        black_input = int(input('X choose your move:\n'))
        return black_input

def is_over(board):
    ''' Function is used to check if the game
    is over by checking if any empty spaces are left
    on the board'''

    for board_space in board:
        if board_space == EMPTY :
            return False
    return True


def get_opposite_turn(turn):
    '''Function is used to find out what the current turn
    is after a player has made their move'''

    if turn == WHITE:
        return BLACK

    elif turn == BLACK:
        return WHITE


def print_board(board):
    '''Function is used to print the board as the game
    is played '''
    print('+-----------------------+')
    for board_space in board:
        print('|'+board_space, end='')
    print('|')
    print('+-----------------------+')


def draw_board(board, gui):
    '''Function takes in the board parameter and checks each character
   and prints it out onto a canvas as the game is played, the gui parameter
   is used to be able to draw the text and rectangles'''
    gui.clear()
    gui.text(250,50,'REVERSI','black', 25)
    gui.line(100,99,590,99,'black')
    gui.line(100,150,590,150,'black')
    gui.line(590,99,590,150,'black')
    i = 0
    while i < 480:
        green_space = gui.rectangle(100 + i,100,50,50,'light green')
        gui.line(100 + (i),100,100 + (i), 150,'black')
        i += 40
    for i in range(0,len(board)):
        if board[i] == 'X':
            gui.text(108+(i*40),105,'X','black',30)
        if board[i] == 'O':
            gui.text(108+(i*40),105,'O','black',30)
    gui.update_frame(45)


def who_is_winner(board):
    '''function is used to see who the winner of the game is.
    Function takes in the parameter board to check how many black pieces
    and how many white pieces there are, if one count is greater than the other
    the greater will win'''

    black_count = 0
    white_count = 0

    for board_space in board:
        if board_space == BLACK:
            black_count += 1
        elif board_space == WHITE:
            white_count += 1

    if white_count > black_count:
        return 'WHITE WINS'

    elif black_count > white_count:
        return 'BLACK WINS'

    elif black_count == white_count:
        return 'THERE WAS A TIE'


def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))

main()