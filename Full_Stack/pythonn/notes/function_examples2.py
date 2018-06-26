# # function_examples_2.py 6/22/18
#
# # default argument value if no argument is passed in
# def greet_human(name='Unknown'):
#     print("Hello {}!".format(name))
#
# greet_human("Chelsea")
# greet_human()
# greet_human("Ian")
#
# # more default argument examples
# def add(num1, num2=2, num3=10):
#     print("num1: {}".format(num1))
#     print("num2: {}".format(num2))
#     print("num3: {}".format(num3))
#     print("sum: {}".format(num1+num2+num3))
#     print("*" * 80)
#
# print(add(5, 3, 0))
# print(add(5, num3=6))
# print(add(num3=1, num1=2, num2=3))
#
# # args comes in as a tuple
# def sum(*args):
#     # print(args)
#     total = 0
#     for i in args:
#         # print(i)
#         total += i
#     print("Total: {}".format(total))
#
# sum(1)
# sum(1, 3)
# sum(1, 9, 12, 99)
#
# # kwargs: key word arguments
# # kwargs is a dictionary
# def show_kwargs(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print('*' * 80)
#         print("The key is: {}".format(key))
#         print("The value is: {}".format(value))
#         print('^' * 80)
#
# # Note: the key should NOT be in quotations
# key1 = "value1"
# show_kwargs(key1=key1, key2="value2")
#
# def greeting(name):
#     if name.lower() == "chris":
#         return "get outta here you!"
#     return "Hey {}!".format(name)
#
# print(greeting("Chris"))
# print(greeting("Jeff"))
#
# RECURSION
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))
#
# # returns the n'th fibonnachi number
# def fibonnachi(n):
#     if n < 2:
#         return 1
#     return fibonnachi(n-1) + fibonnachi(n-2)
#
# print(fibonnachi(10))
