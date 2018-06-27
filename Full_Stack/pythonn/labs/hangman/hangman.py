# hangman.py 6/27/18

import random

def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        wl = []
        for word in f.readlines():
            word = word.replace('\n', '')
            if len(word) > 5:
                wl.append(word)
    return wl

def pick_random_word(word_list):
    return random.choice(word_list)

def user_init_word(word):
    return '{}'.format('-' * len(word))

def replace_blank(correct_word, user_word, letter):
    temp_correct_word = list(correct_word)
    temp_user_word = list(user_word)
    print("Correct word list: {}".format(temp_correct_word))
    for i in range(len(temp_correct_word)):
        if letter == temp_correct_word[i]:
            temp_user_word[i] = letter
    return ''.join(temp_user_word)

def display_word(word):
    temp = word[::]
    return temp.replace('', ' ')

def main():
    word_list = load_words('english.txt')
    correct_word = pick_random_word(word_list)
    user_word = user_init_word(correct_word)
    number_of_guesses = 10

    print("Correct word: {}".format(correct_word))

    while True:
        user_letter = input("What letter would you like to guess (enter to exit)?: ")
        if not user_letter:
            print('Goodbye')
            exit(0)
        else:
            user_word = replace_blank(correct_word, user_word, user_letter)
            print(display_word(user_word))

main()
