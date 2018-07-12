# hangman.py 6/27/18

import random
import string


# creates a word list with words greater than 5 letters
def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        wl = []
        for word in f.readlines():
            word = word.replace('\n', '')
            if len(word) > 5:
                wl.append(word)
    return wl


# picks a random word from the word list
def pick_random_word(word_list):
    return random.choice(word_list)


# user word initially starts off with all blanks
def user_init_word(word):
    return '{}'.format('_' * len(word))


# updates number_of_guesses accordingly
def update_guesses(prevWord, currWord, guesses):
    if prevWord == currWord:
        return (guesses - 1)
    return guesses


# checks if letter is in correct_word and updates user_word accordingly
def replace_blank(correct_word, user_word, letter):
    temp_correct_word = list(correct_word)
    temp_user_word = list(user_word)

    # if it's a correct letter, replace the blank in user word with the letter
    for i in range(len(temp_correct_word)):
        if letter == temp_correct_word[i]:
            temp_user_word[i] = letter

    # return user word
    return ''.join(temp_user_word)


# puts spaces between letters and blanks for display readibility
def display_user_word(word):
    temp = word[::]
    return temp.replace('', ' ')


# check if we ran out of guesses
def isOutOfGuesses(number_of_guesses):
    if number_of_guesses == 0:
        return True
    return False


# check if the user won
def isWon(correct_word, user_word):
    if correct_word == user_word:
        return True
    return False


# check if we want to play again
def play_again():
    while True:
        play_again = input("Would you like to play again?: ")
        if play_again.lower() in ['y', 'yes']:
            break
        elif play_again.lower() in ['n', 'no']:
            print("Thanks for playing. Goodbye!")
            exit(0)
        else:
            print("Not a valid input.")
    main()


def main():
    # initialize things for the game
    word_list = load_words('english.txt')
    correct_word = pick_random_word(word_list)
    user_word = user_init_word(correct_word)
    letters_guessed = []
    number_of_guesses = 10

    print("Welcome to hangman!")
    print(display_user_word(user_word))
    # print("Correct word: {}".format(correct_word))

    while True:
        print()
        user_letter = input("What letter would you like to guess "
                            "(enter to exit)?: ")
        if not user_letter:
            print('Goodbye')
            exit(0)

        # check validity of user input
        elif len(user_letter) > 1 or user_letter not in string.ascii_letters:
            print("That was not a letter.")
            continue

        # valid user input -> lets play!
        elif user_letter in string.ascii_letters and len(user_letter) == 1:
            # keep track of letters guessed
            if user_letter not in letters_guessed:
                letters_guessed.append(user_letter)
            else:
                print("You've already guessed that letter.")
                continue

            # check if the letter was correct and
            # update number_of_guesses accordingly
            prev_user_word = user_word
            user_word = replace_blank(correct_word, user_word, user_letter)
            number_of_guesses = update_guesses(prev_user_word, user_word,
                                               number_of_guesses)

            # display information to user
            print(display_user_word(user_word))
            print("Guesses remaining: {}".format(number_of_guesses))
            print("Letters guessed {}".format(letters_guessed))

            # check if the game is over
            if isOutOfGuesses(number_of_guesses):
                print("You lose. The word was: '{}'".format(correct_word))
                play_again()
            if isWon(correct_word, user_word):
                print("YOU WIN!!!")
                play_again()

main()
