# rot13_cipher.py 6/15/18

######## George's Way (SUPER EASY) ######
import string

print("Hello. This is an encoder.")
rotation_amt = int(input("How many encoding rotations would you like to do?\n> "))
user_input = input("Please type in a sentence you would like to encode.\n> ")
while not user_input.isalpha():
    print("Your input does not have only letters.")
    user_input = input("Please type in a sentence you would like to encode.\n> ")

user_input_lower = user_input.lower()
rot13 = string.ascii_lowercase[rotation_amt:] + string.ascii_lowercase[0:rotation_amt]
encoded_string = ''
for i in range(len(user_input_lower)):
    letter_position = string.ascii_lowercase.find(user_input_lower[i])
    encoded_string += rot13[letter_position]

print(f"The encoded string is: '{encoded_string}'")



######## My way (SUPER DIFFICULT) ##########
# import string
#
# print("Hello. This is an encoder.")
# rotation_amt = int(input("How many encoding rotations would you like to do?\n> "))
# user_input = input("Please type in a sentence you would like to encode.\n> ")
#
# while not user_input.isalpha():
#     print("Your input does not have only letters.")
#     user_input = input("Please type in a sentence you would like to encode.\n> ")
# user_input_lower = user_input.lower()
#
# # rotX: num1, num2, num3
# # rot10: 15, 16, 10
# # rot11: 14, 15, 11
# # rot12: 13, 14, 12
# # rot13: 12, 13, 13
# # rot14: 11, 12, 14
# # rot15: 10, 11, 15
# # rot16:  9, 10, 16
# num1 = (rotation_amt - ((rotation_amt - 13) * 2) - 1)
# num2 = num1 + 1
# num3 = rotation_amt
#
# encoded_string = ''
# for i in range(len(user_input_lower)):
#     letter_position = string.ascii_lowercase.find(user_input_lower[i])
#     if letter_position > num1:
#         rot_position = letter_position - num2
#     else:
#         rot_position = letter_position + num3
#     encoded_string += string.ascii_letters[rot_position].lower()
#
# print(f"The encoded string is: '{encoded_string}'")
