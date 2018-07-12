# deck.py 7/04/18

from card import Card
from random import shuffle, choice


class Deck(object):
    def __init__(self):
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        rank += ['J', 'Q', 'K', 'A']
        suit = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        deck = []

        # build a deck of 52 cards
        # each rank will have 4 different suits
        for i in range(len(rank)):
            for j in range(len(suit)):
                deck.append(Card(rank[i], suit[j]))
        self.deck = deck

    def __repr__(self):
        # go through each card in the deck and appened
        # the string representation of
        # the card to a temp variable.
        temp = ''
        for card in self.deck:
            temp += str(card) + '\n'
        # return the temp variable without the last newline character
        return temp[:-1]

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, position):
        return self.deck[position]

    # shuffle the cards in the deck
    def shuffle(self):
        return shuffle(self.deck)

    # pick a random number between 10 and 40 then cut the deck
    def cut_deck(self):
        cut = choice(range(10, 41))
        self.deck = self.deck[cut:] + self.deck[:cut]

    # return the top card on the deck
    def deal(self):
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
    print("Length of Deck: " + str(len(deck)))
    print("7th Card in Deck: " + str(deck[6]))
    top_card = deck.deal()
    print("Draw Card: " + str(top_card))
