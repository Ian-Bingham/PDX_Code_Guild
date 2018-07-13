# hand.py 7/04/18

from deck import Deck


class Player(object):
    def __init__(self):
        self.hand = []

    def __repr__(self):
        temp = ''
        for card in self.hand:
            temp += str(card) + '\n'
        return temp[:-1]

    def __len__(self):
        return len(self.hand)

    # add card to hand
    def add_card(self, card):
        self.hand.append(card)

    # calculate score of hand
    def score(self):
        # define score conversions - Ace defaults to 11
        score_conversion = {str(key): key for key in range(2, 11)}
        score_conversion.update({'A': 11, 'J': 10, 'Q': 10, 'K': 10})
        num_aces = 0  # keep track of number of Aces in hand
        points = 0  # keep track of points
        # go through each card in the hand and update points / number of Aces
        for card in self.hand:
            points += score_conversion[card.rank]
            if card.rank == 'A':
                num_aces += 1

        # implement Ace as a value of 1 if needed
        if points > 21:
            for i in range(num_aces):
                points -= 10
                if points < 21:
                    break

        return points


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print("Deck\n" + str(deck))
    hand1 = Player()
    while len(hand1) < 5:
        hand1.add_card(deck.deal())
    print("Hand Drawn From Deck\n" + str(hand1))
    print("Length of Hand: " + str(len(hand1)))
    print("Points: " + str(hand1.score()))
