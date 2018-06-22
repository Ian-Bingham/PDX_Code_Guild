import random

def greet(name):
    greetings =["Hi", "Hello", "Hiya"]
    return "{}, {}!".format(random.choice(greetings), name)

# from random import choice
#
# def greet(name):
#     greetings =["Hi", "Hello", "Hiya"]
#     return "{}, {}!".format(choice(greetings), name)

n = input("What is your name?\n> ")
print(greet(n))
print(greet(n))
print(greet(n))
print(greet(n))
print(greet(n))
