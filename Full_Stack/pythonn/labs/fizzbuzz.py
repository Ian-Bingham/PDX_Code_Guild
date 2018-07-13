# fizzbuzz.py 6/29/18


# Given the length of the output of numbers from 1 - n:
# If a number is divisible by 3, append “Fizz” to a list.
# If a number is divisible by 5, append “Buzz” to that same list.
# If a number is divisible by both 3 and 5, append “FizzBuzz” to the list.
# If a number meets none of theese rules, just append the string of the number.
def fizzbuzz(n):
    fizzbuzz_list = []
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif i % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif i % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(str(i))
    return fizzbuzz_list

print(fizzbuzz(20))
