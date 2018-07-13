
from player import Player
from board import Board


def main():
        while True:
            # create players
            playerX = Player('X')
            playerO = Player('O')
            players = [playerX, playerO]
            board = Board()  # initialize board
            player_turn = 0  # track player turn
            print(board)  # display initial board

            # players take turns placing a piece until the game is over
            while True:
                board.move(players[player_turn])
                print(board)
                player_turn = 1 - player_turn
                if board.is_gameover():
                    print("Gameover!")
                    break

            # see if they want to play again
            while True:
                again = input("Would you like to play again? ").lower()
                if again in ['y', 'yes']:
                    break
                elif again in ['n', 'no']:
                    print("Goodbye!")
                    exit(0)
                else:
                    print("Invalid input.")


main()
