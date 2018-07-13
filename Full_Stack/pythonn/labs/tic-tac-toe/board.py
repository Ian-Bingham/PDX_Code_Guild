# board.py 7/10/18

import os


class Board(object):
    # initialize board to underscores
    def __init__(self):
        self.board = {position: '_' for position in range(1, 10)}

    # clear terminal screen and keep print statement at the top
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Tic-Tac-Toe!")

    # print representation of the board
    def __repr__(self):
        self.clear()
        temp = ''
        for i in range(3):
            temp += '\n'
            for j in range(1, 4):
                temp += self.board[(i * 3) + j]
                temp += ' '
        temp += '\n'
        return temp

    # place a token on the board
    def move(self, player):
        while True:  # ask user where they want to place the piece
            position = input("Where would you like to place a piece '{}' "
                             "player (1-9)? ".format(player.token))

            # check validity of input
            if position.isdigit() and 1 <= int(position) <= 9:
                # check if the space is blank. otherwise there's a token
                if self.board[int(position)] == '_':
                    self.board[int(position)] = player.token
                    break
                else:
                    print("That spot is already taken.")
            else:
                print("Please enter a number from 1-9.")

    # check to see if there's a winner
    def calc_winner(self):
        # Rows
        # 123
        # 456
        # 789
        #
        # Columns
        # 147
        # 258
        # 369
        #
        # Diagonals
        # 159
        # 357

        # check rows
        for i in range(3):
            row = ''
            col = ''
            for j in range(3):
                row += self.board[(i * 3) + (j + 1)]  # rows
                col += self.board[(i + 1) + (j * 3)]  # columns
            # check if string is made up of the same character
            if '_' not in list(row):
                if len(set(row)) == 1:
                    # noinspection PyUnboundLocalVariable
                    return self.board[(i * 3) + (j + 1)]
                    # return 'Found rows'
            if '_' not in list(col):
                if len(set(col)) == 1:
                    # noinspection PyUnboundLocalVariable
                    return self.board[(i + 1) + (j * 3)]
                    # return 'Found columns'

        # # check columns
        # for i in range(3):
        #     temp = ''
        #     for j in range(3):
        #         temp += self.board[(i + 1) + (j * 3)]
        #     # check if string is made up of the same character
        #     if '_' not in list(temp):
        #         if len(set(temp)) == 1:
        #             return self.board[(i + 1) + (j * 3)]
        #             # return 'Found columns'

        # check diagonals
        if self.board[5] != '_':
            if self.board[1] == self.board[5] == self.board[9]:
                return self.board[5]
                # return 'Found diagonal'
            if self.board[3] == self.board[5] == self.board[7]:
                return self.board[5]
                # return 'Found diagonal'

        # return none if no one has won
        return None

    def is_full(self):
        for key, value in self.board.items():
            if value == '_':
                return False
        return True

    def is_gameover(self):
        if self.calc_winner() not in [None]:
            print("{} player won!".format(self.calc_winner()))
            return True
        elif self.is_full():
            print("Tie")
            return True
        return False
