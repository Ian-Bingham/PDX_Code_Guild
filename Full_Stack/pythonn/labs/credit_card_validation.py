# credit_card_validation.py 6/21/18

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# 4556737586899855 -> Valid!


def credit_card_validation():
    credit_card_16 = input("Please enter a 16 digit credit card number: ")
    credit_card_16 = list(map(int, list(credit_card_16)))  # convert to list
    check_digit = credit_card_16[-1]  # get last digit
    credit_card_15 = credit_card_16[:-1]  # slice off last digit
    credit_card_15.reverse()  # reverse list
    for i in range(len(credit_card_15)):
        if i % 2 == 0:  # double every other element
            credit_card_15[i] *= 2
        if credit_card_15[i] > 9:  # subtract 9 from numbers over nine
            credit_card_15[i] -= 9

    # check card validity
    if str(sum(credit_card_15))[1] == str(check_digit):
        print("Card number is valid")
    else:
        print("Card number is not valid")

credit_card_validation()
