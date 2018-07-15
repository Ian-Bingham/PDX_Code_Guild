# bogo_sort.py 7/14/18

from random import choice

# Bogo sort is one of the least efficient sorting algorithms imaginable!
# this is just for recursion practice


# generates a list of numbers of length n
# numbers in list are between 0-100
def random_list(n):
    lst = []
    for i in range(n):
        lst.append(choice(range(101)))
    return lst


# shuffles the list by swapping the current index with
# a randomly generated index
def shuffle_nums(nums):
    for i in range(len(nums)):
        new_index = choice(range(len(nums)))
        nums[i], nums[new_index] = nums[new_index], nums[i]
    return nums


# checks if the list is sorted from least to greatest
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


# recursively sort the list by shuffling the list and seeing
# if the shuffled list magically ends up sorting itself
def bogo_sort(nums):
    while not is_sorted(nums):
        shuffled_list = shuffle_nums(nums)
        bogo_sort(shuffled_list)
    return nums


def main():
    num_list = random_list(5)
    print(f"Original list: {num_list}")
    sorted_list = bogo_sort(num_list)
    print(f"Sorted list: {sorted_list}")


main()
