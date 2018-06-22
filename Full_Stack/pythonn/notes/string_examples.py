# """
#
# Author: Ian Bingham
# 06/18/18
# This file is an example of python strings.
#
# """
#
# hello = "Hello"
# print(hello)
# print(hello.lower())
# print(hello.upper())
#
# foo1 = '"Hello", he said.'
# foo2 = "Chris's stuff"
# foo3 = """Portland
#
#         OR"""
# print(foo1)
# print(foo2)
# print(foo3)
#
# greeting = "Hi"
# name = input("What is your name?\n> ")
# print(greeting, name)
# print(greeting + " " + name)
# print("{} {}!".format(greeting, name))
# print("{a} {b}~".format(a=greeting, b=name))
# print("{1} {0} {0} {1}...".format(greeting, name))
# print(f"{greeting} {name} :)")
#
# words = "i really like to code."
# fruit = "apple"
# print(fruit.center(20, '*')) # pads the word to fit 20 characters by filling in with the * character
# print(words.capitalize()) # capitalizes the first letter and makes everything else lowercase
# print(words.count('i', 1, 4)) # counts the number of characters from the given index up to the stop point
# print(words.endswith("code."))
# print(words.find('o', 16)) # returns first occurance of character starting at given index. returns -1 if not found
# print(words.isalnum()) # is alpha numeric
# print(words.replace('l', '$'))
# print(words.replace(' ', '').isalpha()) # spaces do not count
# print(words.islower())
# print(words.split()) # splits by spaces by default. puts it in a list
# print(words.title()) # capitalizes first letter in every word
# print(words.title().swapcase())
#
# nums = "123a45"
# if nums.isdigit():
#     nums = int(nums)
# else:
#     raise ValueError("must be all numbers")
#
# story = ["the", "cat", "in", "the", "hat"]
# whole_story = '-'.join(story) # joins each item in the list with '-' in between
# print(story)
# print(whole_story)
