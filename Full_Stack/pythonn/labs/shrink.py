# shrink.py 6/29/18

# gets the integers in a string
def get_nums(sentence):
    num_list = [int(num) for num in sentence.split() if num.isdigit()]
    return num_list

def add_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

# adds numbers in a list
# if the sum is not one digit, then add the digits of the sum
def shrink(num_list):
    summ = add_list(num_list)
    if summ > 9:
        return shrink([int(digit) for digit in str(summ)])
    return summ

def main():
    sentence = "1 + 2 + 3 + 4 + 5"
    num_list = get_nums(sentence)
    print("{} shrunk is {}".format(add_list(num_list), shrink(num_list))) # 15 -> 6

    sentence = "1 + 2 + 3 + 4 + 5 + 6"
    num_list = get_nums(sentence)
    print("{} shrunk is {}".format(add_list(num_list), shrink(num_list))) # 21 -> 3

    sentence = "1 + 2 + 3 + 4 + 5 + 6 + 7"
    num_list = get_nums(sentence)
    print("{} shrunk is {}".format(add_list(num_list), shrink(num_list)))  # 28 -> 10 -> 1

main()
