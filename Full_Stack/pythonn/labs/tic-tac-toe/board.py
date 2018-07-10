# board.py 7/10/18

from player import Player

class Board(object):
    def __init__(self):
        self.board = {position:'_' for position in range(1, 10)}

    def __repr__(self):
        temp = ''
        for i in range(3):
            temp += '\n'
            for j in range(1, 4):
                temp += self.board[(i * 3) + j]
                temp += ' '
        temp += '\n'
        return temp

    def move(self, player):
        while True:
            position = input("Where would you like to place a piece '{}' player (1-9)? ".format(player.token))
            if position.isdigit() and 1 <= int(position) <= 9:
                if self.board[int(position)] == '_':
                    self.board[int(position)] = player.token
                    break
                else:
                    print("That spot is already taken.")
            else:
                print("Please enter a number from 1-9.")

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
            temp = ''
            for j in range(1, 4):
                temp += self.board[(i * 3) + j]
            # check if string is made up of the same character
            if '_' not in list(temp):
                if len(set(temp)) == 1:
                    return self.board[(i * 3) + j]
                    # return 'Found rows'

        # check columns
        for i in range(1, 4):
            temp = ''
            for j in range(3):
                temp += self.board[i + (j * 3)]
            # check if string is made up of the same character
            if '_' not in list(temp):
                if len(set(temp)) == 1:
                    return self.board[i + (j * 3)]
                    # return 'Found columns'

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
        if self.calc_winner() != None:
            print("{} player won!".format(self.calc_winner()))
            return True
        elif self.is_full():
            print("Tie")
            return True
        return False
