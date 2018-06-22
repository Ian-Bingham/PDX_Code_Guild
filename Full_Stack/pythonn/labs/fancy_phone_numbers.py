# fancy_phone_numbers.py 6/20/18

def format_phone_number(phone_number):
    formatted_number = format(int(phone_number[:-1]), "_").replace("_", "-") + phone_number[-1]
    print(formatted_number)

phone_number = input("Please input an all digits phone number: ")
format_phone_number(phone_number)
