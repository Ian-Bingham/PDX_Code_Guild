# card.py 7/04/18

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

if __name__ == '__main__':
    card1 = Card('5', 'Hearts')
    print(card1.rank, "of", card1.suit)
    card2 = Card('Q', 'Clubs')
    print(card2.rank, "of", card2.suit)
    card3 = Card('A', 'Diamonds')
    print(card3.rank, "of", card3.suit)
