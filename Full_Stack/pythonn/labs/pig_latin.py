# pig_latin.py 06/19/18

def pig_latin():
    print("Hello. This program changes words to pig latin.")

    word = input("Please type in a word: ")

    if word[0].lower() in ["a", "e", "i", "o", "u"]: # if the first letter is a vowel
            newWord = word + "yay"
    elif word[0] not in ["a", "e", "i", "o", "u"]: # if the first letter is a consonant
        index = 0
        for i in word: # keep track of how many consonants are at the beginning
            if i.lower() not in ["a", "e", "i", "o", "u"]:
                index += 1
            else:
                break
        if word[0].isupper(): # maintain proper capitalization
            newWord = word[index].upper() + (word[index+1:] + word[:index] + "ay").lower()
        else:
            newWord = word[index:] + word[:index] + "ay"

    print("{} in pig latin is {}.".format(word, newWord))

pig_latin()
