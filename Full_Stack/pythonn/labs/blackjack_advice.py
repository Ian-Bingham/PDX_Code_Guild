# blackjack_advice.py 6/29/18

# Less than 17, advise to “Hit”
# Greater than or equal to 17, but less than 21, advise to “Stay”
# Exactly 21, advise “Blackjack!”
# Over 21, advise “Already Busted”

# initialize card values
card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]}
for i in range(10):
    card_values['{}'.format(i + 2)] = i + 2

def print_hit():
    print("You should Hit.")

def print_stand():
    print("You should Stand.")

def print_double():
    print("You should Double Down.")

def print_blackjack():
    print("Blackjack!!!")

def print_bust():
    print("You Bust.")

while True:
    first_card = input("What's your first card? ").upper()
    second_card = input("What's your second card? ").upper()
    dealer_card = input("What is the dealer showing? ").upper()

    if dealer_card == 'A':
        dealer_card_value = card_values[dealer_card][1]
    else:
        dealer_card_value = card_values[dealer_card]

    # determine if 'A' should be 1 or 11
    if first_card != 'A' and second_card != 'A':
        first_card_value = card_values[first_card]
        second_card_value = card_values[second_card]
    elif first_card == 'A' and second_card == 'A':
        first_card_value = card_values[first_card][0]
        second_card_value = card_values[second_card][1]
    else:
        if first_card == 'A':
            if card_values[first_card][1] + card_values[second_card] <= 21:
                first_card_value = card_values[first_card][1]
            else:
                first_card_value = card_values[first_card][0]
            second_card_value = card_values[second_card]
        if second_card == 'A':
            if card_values[first_card] + card_values[second_card][1] <= 21:
                second_card_value = card_values[second_card][1]
            else:
                second_card_value = card_values[second_card][0]
            first_card_value = card_values[first_card]

    print("You have {}".format(first_card_value + second_card_value))
    print("Dealer has {}".format(dealer_card_value))

    # if first_card_value + second_card_value < 17:
    #     print_hit()
    # elif 17 < first_card_value + second_card_value < 21:
    #     print_stand
    # elif first_card_value + second_card_value == 21:
    #     print_blackjack()
    # elif first_card_value + second_card_value > 21:
    #     print_bust()

    # pair values
    if first_card_value == second_card_value:
        pass


    # hard values
    elif first_card_value != 11 and second_card_value != 11:
        if 5 <= first_card_value + second_card_value <= 8:
            print_hit()
        if first_card_value + second_card_value == 9:
            if dealer_card_value in [3, 4, 5, 6]:
                print_double()
            else:
                print_hit()
        if first_card_value + second_card_value in [10, 11]:
            if dealer_card_value not in [10, 11]:
                print_double()
            else:
                print_hit()
        if first_card_value + second_card_value == 12:
            if dealer_card_value in [4, 5, 6]:
                print_stand()
            else:
                print_hit()
        if 13 <= first_card_value + second_card_value <= 16:
            if dealer_card_value in [2, 3, 4, 5, 6]:
                print_stand()
            else:
                print_hit()
        if 17 <= first_card_value + second_card_value <= 21:
            if first_card_value + second_card_value == 21:
                print_blackjack()
            else:
                print_stand()
