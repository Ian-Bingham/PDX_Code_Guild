# prime_numbers.py 7/16/18


# create a list of numbers
def create_nums(n):
    tmp = []
    for i in range(2, n + 1):
        tmp.append(i)
    return tmp


# recursive function to find prime numbers
def find_primes(num_list, prime_list):
    prime_list.append(num_list.pop(0))  # get the most recently found prime number
    if not num_list:  # check if we have any more numbers to check
        return  # Note: we are altering the parameters directly so we do not need to return anything

    # divide each number by the prime number. if we get a remainder, then it's a composite number. remove it
    for num in num_list[1:]:
        if num % prime_list[-1] == 0:
            num_list.remove(num)
    find_primes(num_list, prime_list)


def main():
    number = int(input("What number do you want to find primes up to? "))
    nums = create_nums(number)
    primes = []
    find_primes(nums, primes)
    print(f"Prime list: {primes}")


main()
