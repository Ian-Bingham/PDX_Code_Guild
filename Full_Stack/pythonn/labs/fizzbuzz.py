# fizzbuzz.py 6/29/18

def fizzbuzz(n):
    fizzbuzz_list = []
    for i in range(n):
        j = i + 1
        if j % 3 == 0 and j % 5 == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif j % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif j % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(str(j))
    return fizzbuzz_list

print(fizzbuzz(20))
