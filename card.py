class Card(object):
    """ THIS IS A CARD """

    def __init__(self, index):
        self.index = index
        self.card_value = index % 13
        self.suit_value = index % 4

    def raw_info(self):
        if self.card_value == 0:
            return (13, self.suit_value)
        return (self.card_value, self.suit_value)

    def __repr__(self):
        if self.suit_value == 0:
            suit = 'hearts'
        elif self.suit_value == 1:
            suit = 'diamonds'
        elif self.suit_value == 2:
            suit = 'clubs'
        else:
            suit = 'spades'

        if self.card_value == 0:
            value = 'ace'
        elif self.card_value == 10:
            value = 'jack'
        elif self.card_value == 11:
            value = 'queen'
        elif self.card_value == 12:
            value = 'king'
        else:
            value = self.card_value + 1

        return 'The %s of %s' %(value, suit)
