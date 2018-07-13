# card.py 7/04/18


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


if __name__ == '__main__':
    card1 = Card('5', 'Hearts')
    print(card1)
    card2 = Card('Q', 'Clubs')
    print(card2)
    card3 = Card('A', 'Diamonds')
    print(card3)
