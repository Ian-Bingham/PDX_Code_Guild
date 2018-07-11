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
        score_conversion.update({'A': 11, 'J': 10, 'Q': 10, 'K': 10}) # Ace defaults to 11
        numAces = 0
        points = 0
        for card in self.hand:
            temp_points = points
            newVal = score_conversion[card.rank]
            if card.rank == 'A':
                numAces += 1
            temp_points += newVal
            points = temp_points

        # implement Ace as a value of 1 if needed
        if points > 21:
            for i in range(numAces):
                points -= 10
                if points < 21:
                    break

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
