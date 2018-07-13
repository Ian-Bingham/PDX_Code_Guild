# fancy_phone_numbers.py 6/20/18


# number example: 111-2222 OR 333-444-5555
# place underscore after every third number up to the last digit
# replace underscore with hyphen
# append last number
def format_phone_number(phone_number):
    formatted_number = format(int(phone_number[:-1]), "_").replace("_", "-") \
                              + phone_number[-1]
    print(formatted_number)

phone_number = input("Please input an all digits phone number: ")
format_phone_number(phone_number)
