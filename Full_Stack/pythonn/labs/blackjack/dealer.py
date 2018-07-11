# dealer.py 7/10/18

from hand import Hand

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def visible_card(self):
        return "{} of {}".format(self.hand[1].rank, self.hand[1].suit)

    def visible_score(self):
        score_conversion = {str(key):key for key in range(2, 11)}
        score_conversion.update({'A': 11, 'J': 10, 'Q': 10, 'K': 10})
        return "{}".format(score_conversion[self.hand[1].rank])
