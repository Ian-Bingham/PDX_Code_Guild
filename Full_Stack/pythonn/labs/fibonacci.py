# fibonacci.py 7/13/18


# optimizes the fibonacci function by saving results into a dictionary
# that way we don't need to recalculate things
def memoize(fn):
    memo = {}

    def call(x):    # x is referring to the PARAMETER in the fn function
                    # in this case it refers to the n parameter in fibonacci
        if x not in memo:
            memo[x] = fn(x)
        return memo[x]
    return call


@memoize  # think of this decorator function as a wrapper function
# calculates the n'th + 1 fibonacci number
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))
