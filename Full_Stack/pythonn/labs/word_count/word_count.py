# word_count.py 6/22/18

from operator import itemgetter
import string


def clean_text(filename):
    # lowercase everything, remove punctions, then create a list of words
    translator = str.maketrans('', '', string.punctuation)
    with open(filename, 'r', encoding="UTF-8") as f:
        text = f.read().lower().translate(translator)
        word_list = text.split()
        return word_list


def count_words(word_list):
    # find all of the unique words and keep a word count: {word: wordcount}
    unique_word_dict = {}
    for word in word_list:
        if word not in unique_word_dict.keys():
            unique_word_dict[word] = 1
        else:
            unique_word_dict[word] += 1
    return unique_word_dict


def top_words(unique_word_dict, num):
    # create a list of tuples from the unique_word_dict: (word, wordCount)
    unique_word_list = []
    for key, value in unique_word_dict.items():
        unique_word_list.append((key, value))

    # sort the list of tuples in ascending order
    # by the second value in the tuple
    unique_word_list.sort(key=itemgetter(1))
    top_words = []
    for i in range(num):
        top_words.append(unique_word_list[-num + i])

    # reverse the list of tuples so the top 10 words are first
    top_words.reverse()
    for word, wordCount in top_words:
        print("'{}' was seen {} times.".format(word, wordCount))


def main():
    filename = input("What is the name of the file?: ")
    wl = clean_text(filename)
    unique_word_dict = count_words(wl)
    number = input("How many top words do you want to see?: ")
    top_words(unique_word_dict, int(number))

main()

# # Chris's version 6/25/18
# from string import punctuation, ascii_letters
# from operator import itemgetter
#
#
# def open_text(filename, enc='utf-8'):
#     """
#     Opens a text file and returns all of the text as a string.
#     """
#     with open(filename, 'r', encoding=enc) as f:
#         return f.read()
#
# def strip_punct(text):
#     # for i in punctuation + '“”—,’‘':
#     #     if i != "'":
#     #         print(i)
#     #         text = text.replace(i, '')
#     new_text = ''
#     for i in text:
#         if i in ascii_letters+"' \n\t\r—":
#             if i == '—':
#                 new_text += ' '
#                 continue
#             new_text += i
#     return new_text
#
# def clean_text(text):
#     stripped_punct = strip_punct(text)
#     word_list = stripped_punct.lower().split()
#     return word_list
#
# def count_words(wl):
#     wc_dict = {}
#     for i in wl:
#         if i in wc_dict:
#             wc_dict[i] += 1
#         else:
#             wc_dict[i] = 1
#     return wc_dict
#
#
# def to_n(wc, n=10):
#     top_list = sorted(wc.items(), key=itemgetter(1), reverse=True)
#     return top_list[:n]
#
# def main():
#     fn = input('What is the name of your file?: ')
#     t = open_text(fn)
#     wl = clean_text(t)
#     wc = count_words(wl)
#     number = input('How many do you want to see?: ')
#     for word, count in to_n(wc, int(number)):
#         print("'{}' was seen {} times.".format(word, count))
#
# main()
