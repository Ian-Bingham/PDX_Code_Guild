# card.py 7/04/18

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

card1 = Card('5', 'Hearts')
print(card1.rank, "of", card1.suit)
