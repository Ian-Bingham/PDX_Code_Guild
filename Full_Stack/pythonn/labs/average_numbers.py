# average_numbers.py 6/21/18

# # Version 1 Method 1
# def calculate_average(nums):
#     average = sum(nums) / len(nums)
#     print(average)
#
# # Version 1 Method 2
# def calculate_average(nums):
#     summ = 0
#     for num in nums:
#         summ += num
#     average = summ / len(nums)
#     print(average)

# nums = [5, 0, 8, 3, 4, 1, 6]
# calculate_average(nums)


# Version 2
def calculate_average():
    nums = []
    while True:
        user_input = input("Enter a number to add to the list or type "
                           "(d)one when finished: ")
        if user_input.lower() in ["d", "done"]:
            average = sum(nums) / len(nums)
            print(average)
            return
        nums.append(int(user_input))


calculate_average()
