# dealer.py 7/10/18

from player import Player


# dealer inherits from Hand
class Dealer(Player):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()

    # only show the second card in the dealer's hand
    def visible_card(self):
        # noinspection PyUnresolvedReferences,PyUnresolvedReferences
        return "{} of {}".format(self.hand[1].rank, self.hand[1].suit)

    # only show the value of the second card in the dealer's hand
    def visible_score(self):
        score_conversion = {str(key): key for key in range(2, 11)}
        score_conversion.update({'A': 11, 'J': 10, 'Q': 10, 'K': 10})
        # noinspection PyUnresolvedReferences
        return "{}".format(score_conversion[self.hand[1].rank])
