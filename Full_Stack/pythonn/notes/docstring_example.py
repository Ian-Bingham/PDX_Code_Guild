# doctstring_test.py 7/10/18

"""
knights() Doctest
>>> knights()
Knights who say Ni!

add() Doctest
>>> add(5, 2)
7

>>> add(-1, 3)
2

>>> add(-1, -4)
-5
"""

# the below would produce a failure in the doctest:
# >>> add(1, 5)
# 10
#
# this is the output if the above docstring is executed:
# File "docstring_example.py", line 15, in __main__
# Failed example:
#     add(-1, -4)
# Expected:
#     -10
# Got:
#     -5
# **********************************************************************
# 1 items had failures:
#    1 of   4 in __main__
# ***Test Failed*** 1 failures.

def knights():
    print("Knights who say Ni!")

def add(a, b):
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
