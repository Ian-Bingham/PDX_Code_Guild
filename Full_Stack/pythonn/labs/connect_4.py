# connect_4.py 6/28/18

import os

# global variables
board_height = 6
board_width = 7
player = ['☻', '☺']


# initialize the board to all underscores
def init_board(board):
    for i in range(board_height):
        board.append([])  # create a row
        for j in range(board_width):
            board[i].append('_')  # fill in the row with -'s
    return board


# clear terminal screen and keep print statement at the top
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Connect Four!")


# print a representation of the board
def print_board(board):
    clear()
    print()
    print('1 2 3 4 5 6 7', end=' ')  # column numbers displayed for user
    for i in range(board_height):
        print()
        for j in range(board_width):
            print(board[i][j], end=' ')
    print()
    print()


# place a piece on the board
def make_move(board, move, player):
    for i in range(board_height):
        for j in range(board_width):
            # find the next open spot in the 'move' column
            if board[board_height - i - 1][move] == '_':
                board[board_height - i - 1][move] = player
                return board


# check for a vertical win
def check_vertical_win(board, player):
    tmp = []

    # get the string representation of each column
    # if there are four of the same token in a row then player wins
    for j in range(board_width):
        for i in range(board_height):
            tmp.append(board[board_height - i - 1][j])
        if (player * 4) in ''.join(tmp):
            return True
        else:
            tmp = []
    return False


# check for a horizontal win
def check_horizontal_win(board, player):
    tmp = []

    # get the string representation of each row
    # if there are four of the same token in a row then player wins
    for i in range(board_height):
        for j in range(board_width):
            tmp.append(board[board_height - i - 1][j])
        if (player * 4) in ''.join(tmp):
            return True
        else:
            tmp = []
    return False


# check for a diagonal win
def check_diagonal_win(board, player):
    tmp1 = []

    # check bot left to up right diagonal '/'
    # get the string representation of each '/' diagonal
    # if there are four of the same token in a row then player wins
    for i in range(board_height - 3):
        for j in range(board_width - 3):
            tmp1.append(board[board_height - i - 1][j])
            tmp1.append(board[board_height - i - 2][j + 1])
            tmp1.append(board[board_height - i - 3][j + 2])
            tmp1.append(board[board_height - i - 4][j + 3])
            if (player * 4) in ''.join(tmp1):
                return True
            else:
                tmp1 = []

    tmp2 = []
    # check top left to bot right diagonal '\'
    # get the string representation of each '\' diagonal
    # if there are four of the same token in a row then player wins
    for i in range(board_height - 3):
        for j in range(board_width - 3):
            tmp2.append(board[i][j])
            tmp2.append(board[i + 1][j + 1])
            tmp2.append(board[i + 2][j + 2])
            tmp2.append(board[i + 3][j + 3])
            if (player * 4) in ''.join(tmp2):
                return True
            else:
                tmp2 = []
    return False


# check each win combination
def check_win(board, player):
    if check_vertical_win(board, player) \
            or check_horizontal_win(board, player) \
            or check_diagonal_win(board, player):
        return True
    return False


def main():
    # initialize the board
    board = []
    board = init_board(board)
    player_turn = 0  # track player turn

    # make move and switch player turn until someone wins
    while True:
        move = input("What column would '{}' like to place a piece?: "
                     .format(player[player_turn]))
        if move.isdigit():
            if int(move) - 1 in range(7):
                board = make_move(board, int(move) - 1, player[player_turn])
                print_board(board)
                if check_win(board, player[player_turn]):
                    print("Congrats, {}. You won!!!"
                          .format(player[player_turn]))
                    exit(0)
                player_turn = 1 - player_turn
            else:
                print("That was not a valid column number.")
        else:
            print("That was not a number.")

main()
