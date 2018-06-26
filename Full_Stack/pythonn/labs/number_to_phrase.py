# number_to_phrase.py 6/21/18

ones_place_dict = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

teens_dict = {  10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens_place_dict = { 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

# roman_numerals_dict = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 50: 'L', 100: 'C'}
roman_numerals_dict = { 100: 'C', 50: 'L', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def number_to_phrase():
    while True:
        user_input = input("Enter a number between 1-999 (or enter to quit): ")

        if not user_input:
            print("Goodbye")
            exit(0)

        if user_input.isdigit() and len(user_input) < 3:
            print("{} in English is '{}'".format(user_input, number_to_phrase_1_99(user_input)))
        elif user_input.isdigit() and len(user_input) == 3:
            print("{} in English is '{}'".format(user_input, number_to_phrase_100_999(user_input)))
        else:
            print("That was not a number between 1-999.")
            number_to_phrase()

def number_to_phrase_1_99(number):
    if int(number) < 10:
        return ones_place_dict[int(number)]
    elif 10 <= int(number) < 20:
        return teens_dict[int(number)]
    else:
        if number[-1] == "0":
            return tens_place_dict[int(number[0])]
        else:
            return tens_place_dict[int(number[0])] + '-' + ones_place_dict[int(number[-1])]

def number_to_phrase_100_999(number):
    if int(number) % 100 == 0:
        return ones_place_dict[int(number[0])] + " hundred"
    hundreds_place = ones_place_dict[int(number[0])] + " hundred "
    return hundreds_place + number_to_phrase_1_99(number[1:])

number_to_phrase()

# # NOT WORKING
# def number_to_roman_numerals(number):
#     leftover = 0
#     for keys in roman_numerals_dict.keys():
#         quotient, x = divmod(int(number), keys)
#         leftover -= keys * quotient
#         if leftover > 0:
#             number_to_roman_numerals(leftover)
#         else:
#             return output
#
# # number_to_phrase()
# output = ''
# user_input = input("Enter a number between 1-999 (or enter to quit): ")
# print("{} in English is '{}'".format(user_input, number_to_roman_numerals(user_input)))
