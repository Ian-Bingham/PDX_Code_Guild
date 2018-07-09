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

    def __repr__(self):
        temp = ''
        for i in range(len(self.deck)):
            temp += '{} of {}\n'.format(self.deck[i].rank, self.deck[i].suit)
        return temp

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, position):
        return self.deck[position]
        # deck[5]

    def shuffle(self):
        return shuffle(self.deck)

    def cut_deck(self):
        cut = choice(range(10, 52))
        self.deck = self.deck[cut:] + self.deck[:cut]

    def draw_card(self):
        return self.deck.pop(0)

if __name__ == '__main__':
    deck = Deck()
    print("Deck")
    print(deck)

    print('*' * 80)
    deck.shuffle()
    print("Shuffled Deck")
    print(deck)

    print('*' * 80)
    deck.cut_deck()
    print("Cut Deck")
    print(deck)

    print('*' * 80)
    print("Length of Deck:", str(len(deck)))
    print("7th Card in Deck:", deck[6])
    top_card = deck.draw_card()
    print("Draw Card:", top_card)
