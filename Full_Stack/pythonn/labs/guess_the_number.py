# guess_the_number.py 6/11/18

import random

computer_number = random.randint(1, 10)
print("Computer number is: " + str(computer_number))
user_guess = input("Please guess a number between 1 and 10.\n> ")

# # version 1 - 10 guesses
# max_guesses = 10
# i = 0
# while True:
#     if i < max_guesses - 1 and int(user_guess) == computer_number:
#         print("You win!")
#         break
#     elif i < max_guesses - 1 and int(user_guess) != computer_number:
#         print("Nope! Try again!")
#         i += 1
#         user_guess = input("Please guess a number between 1 and 10.\n> ")
#     else:
#         print(f"Sorry. You didn't guess the number within "
#               "{max_guesses} guesses.")
#         print("You lose.")
#         break

# # version 2 - unlimited guesses
# i = 0
# while True:
#     if int(user_guess) == computer_number:
#         print("You win!")
#         print(f"You guessed the number in {i + 1} tries.")
#         break
#     else:
#         print("Nope! Try again!")
#         i += 1
#         user_guess = input("Please guess a number between 1 and 10.\n> ")

# # version 3 - tell user if too high or too low
# i = 0
# while True:
#     if int(user_guess) == computer_number:
#         print("You win!")
#         print(f"You guessed the number in {i + 1} tries.")
#         break
#     elif int(user_guess) < computer_number:
#         print("Too low! Guess again.")
#         i += 1
#         user_guess = input("Please guess a number between 1 and 10.\n> ")
#     elif int(user_guess) > computer_number:
#         print("Too high! Guess again.")
#         i += 1
#         user_guess = input("Please guess a number between 1 and 10.\n> ")


# version 4 - tell user if current guess is closer than last
last_difference = 0


def closer(last_difference):
    if abs(int(user_guess) - computer_number) < last_difference:
        print("Warmer.")
    elif abs(int(user_guess) - computer_number) > last_difference:
        print("Closer.")
    else:
        print("The number is in the middle of your last two guesses!")
    last_difference = abs(int(user_guess) - computer_number)
    return last_difference

i = 0
while True:
    if int(user_guess) == computer_number:
        print("You win!")
        print(f"You guessed the number in {i + 1} tries.")
        break
    elif int(user_guess) < computer_number:
        print("Too low! Guess again.")
        i += 1
        last_difference = closer(last_difference)
        user_guess = input("Please guess a number between 1 and 10.\n> ")
    elif int(user_guess) > computer_number:
        print("Too high! Guess again.")
        i += 1
        last_difference = closer(last_difference)
        user_guess = input("Please guess a number between 1 and 10.\n> ")
