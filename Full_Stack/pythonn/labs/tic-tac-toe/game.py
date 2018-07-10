
from player import Player
from board import Board

def main():
        while True:
            print("Welcome to Tic Tac Toe!")
            playerX = Player('X')
            playerO = Player('O')
            players = [playerX, playerO]
            board = Board()
            player_turn = 0
            print(board)
            while True:
                board.move(players[player_turn])
                print(board)
                player_turn = 1 - player_turn
                if board.is_gameover():
                    print("Gameover!")
                    break

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
