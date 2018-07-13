# pick6.py 6/21/18

from random import choice

# {matches: earnings}
monatary_winnings = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000,
                     5: 1000000, 6: 25000000}
ticket_price = -2
num_simulations = 100000


# pick 6 random numbers from 1-99
def pick6():
    nums = []
    for i in range(0, 6):
        nums.append(choice(range(1, 100)))
    return nums


# check number of matches in both lists
def earnings(winning_nums, ticket_nums):
    matches = 0
    for i in range(0, 6):
        if winning_nums[i] == ticket_nums[i]:
            matches += 1
    return monatary_winnings[matches]


def play_pick6():
    # keep track of winnings and balance
    balance = 0
    winnings = 0
    winning_nums = pick6()
    for i in range(0, num_simulations):
        winnings = earnings(winning_nums, pick6())
        balance += ticket_price + winnings

    # calculate expenses and ROI
    expenses = ticket_price * num_simulations
    ROI = (winnings - expenses) / expenses

    print("----- Results after {} simulations -----".format(num_simulations))
    print("Your balance is ${}".format(balance))
    print("Your ROI is ${}".format(ROI))

play_pick6()
