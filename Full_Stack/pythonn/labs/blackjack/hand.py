# hand.py 7/04/18

class Hand(object):
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def create_hand(self):
        while True:
            while True:
                rank = input("What rank would you like for the card? ")
                if rank.upper() not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                    print("Invalid rank.")
                    continue
                break

            while True:
                suit = input("What suit would you like for the card? ")
                if suit.capitalize() not in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
                    print("Invalid suit.")
                    continue
                 break

            user_hand = Hand()
            user_hand.hand.append(Card(rank, suit))

            while True:
                again = input("Would you like to add another card? ")
                if again.lower() in ['y', 'yes']:
                    break
                elif again.lower() in ['n', 'no']:
                    print("Hand created.")
                    return user_hand
                else:
                    print("Invalid option.")
