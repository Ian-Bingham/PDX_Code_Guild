# compute_ari.py 6/29/18

# Formula: https://en.wikipedia.org/api/rest_v1/media/math/render/svg/
# 878d1640d23781351133cad73bdf27bdf8bfe2fd

from math import ceil

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
     14: {'ages': '18-22', 'grade_level':      'College'}
}


# get a list of words from the file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        word_list = f.read().rstrip().split()
        return word_list


# count the number of periods to (roughly) get the number of sentences
def count_sentences(word_list):
    count = 0
    for word in word_list:
        if '.' in word:
            count += 1
    return count


# count the number of characters
def count_characters(word_list):
    total = 0
    for word in word_list:
        total += len(word)
    return total


# compute ari score using the given equation
def compute_ari(characters, words, sentences):
    return ceil(4.71 * (characters / words) + 0.5 *
                (words / sentences) - 21.43)


def main():
    book = 'War and Peace'
    word_list = read_file('./word_count/war_and_peace.txt')
    num_characters = count_characters(word_list)
    num_words = len(word_list)
    num_sentences = count_sentences(word_list)
    ari = compute_ari(num_characters, num_words, num_sentences)

    if ari > 14:
        ari = 14

    grade = ari_scale[ari]['grade_level']
    age = ari_scale[ari]['ages']

    print("The ARI for {} is {}.".format(book, ari))
    print("This corresponds to a(n) {} level of difficulty "
          "that is suitable for an average person {} years old."
          .format(grade, age))

main()
