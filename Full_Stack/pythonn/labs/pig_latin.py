# pig_latin.py 06/19/18


# If the first letter is a consonant, move it to the end.
# Add “ay” to the end of that.
# If the first letter is a vowel, just ad “yay” to the end.
def pig_latin():
    print("Hello. This program changes words to pig latin.")

    word = input("Please type in a word: ")

    # check if the first letter is a vowel
    if word[0].lower() in ["a", "e", "i", "o", "u"]:
            newWord = word + "yay"

    # check if the first letter is a consonant
    elif word[0] not in ["a", "e", "i", "o", "u"]:
        # keep track of how many consonants are at the beginning
        index = 0
        for i in word:
            if i.lower() not in ["a", "e", "i", "o", "u"]:
                index += 1
            else:
                break
        if word[0].isupper():  # maintain proper capitalization
            newWord = word[index].upper() + \
                     (word[index+1:] + word[:index] + "ay").lower()
        else:
            newWord = word[index:] + word[:index] + "ay"

    print("{} in pig latin is {}.".format(word, newWord))

pig_latin()
