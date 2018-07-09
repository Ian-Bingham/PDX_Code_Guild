# hand.py 7/04/18

from card import Card
from deck import Deck

class Hand(object):
    def __init__(self):
        self.hand = []

    def __repr__(self):
        temp = ''
        for card in self.hand:
            temp += str(card) + '\n'
        return temp[:-1]

    def __len__(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def score(self):
        score_conversion = {str(key):key for key in range(2, 11)}
        score_conversion.update({'A': 1, 'J': 10, 'Q': 10, 'K': 10})
        points = 0
        for card in self.hand:
            points += score_conversion[card.rank]
        return points

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print("Deck\n" + str(deck))
    hand1 = Hand()
    while len(hand1) < 5:
        hand1.add_card(deck.deal())
    print("Hand Drawn From Deck\n" + str(hand1))
    print("Length of Hand: " + str(len(hand1)))
    print("Points: " + str(hand1.score()))

    # hand2 = Hand()
    # hand2.create_hand()
    # print("Self Created Hand\n", hand2)
    # print("Length of Hand", str(len(hand2)))
    # print("Points " + str(hand2.score()))
