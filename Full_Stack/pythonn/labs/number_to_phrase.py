# number_to_phrase.py 6/21/18

ones_place_dict = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

teens_dict = {  10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens_place_dict = { 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def number_to_phrase():
    while True:
        user_input = input("Enter a number between 0-99 (or enter to quit): ")

        if not user_input:
            print("Goodbye")
            exit(0)

        if user_input.isdigit() and len(user_input) < 3:
            if int(user_input) < 10:
                print("{} in English is {}".format( int(user_input),
                                                    ones_place_dict[int(user_input)]))
            elif 10 <= int(user_input) < 20:
                print("{} in English is {}".format( int(user_input),
                                                    teens_dict[int(user_input)]))
            else:
                if user_input[-1] == "0":
                    print("{} in English is {}".format( int(user_input),
                                                        tens_place_dict[int(user_input[0])]
                                                        ))
                else:
                    print("{} in English is {}-{}".format(   int(user_input),
                                                            tens_place_dict[int(user_input[0])],
                                                            ones_place_dict[int(user_input[-1])]
                                                        ))
        else:
            print("That was not a number between 0-99.")
            number_to_phrase()

number_to_phrase()
