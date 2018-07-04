# deck.py 7/04/18

from card import Card
from random import shuffle, choice

class Deck(object):
    def __init__(self):
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        deck = []

        for i in range(len(rank)):
            for j in range(len(suit)):
                deck.append(Card(rank[i], suit[j]))
        self.deck = deck

    def shuffle(self):
        return shuffle(self.deck)

    def print_deck(self):
        for i in range(len(self.deck)):
            print('{} of {}'.format(self.deck[i].rank, self.deck[i].suit))

    def cut_deck(self):
        cut = choice(range(52))
        self.deck = self.deck[cut:] + self.deck[:cut]

    def draw_card(self):
        return self.deck.pop(0)

# deck = Deck()
# deck.print_deck()
# print('*' * 80)
# deck.shuffle()
# deck.print_deck()
# print('*' * 80)
# deck.cut_deck()
# deck.print_deck()
# print('*' * 80)
# top_card = deck.draw_card()
# print(top_card.rank, top_card.suit)
