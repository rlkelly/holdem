import random

from models.card import Card


class Deck(object):
    def __init__(self):
        self.__deck = [Card(index) for index in range(52)]
        super(Deck, self).__init__()

    def cut(self, value):
        return self.__deck[:value], self.__deck[value:]

    def shuffle(self):
        return random.shuffle(self.__deck)

    def remove_top_card(self):
        return self.__deck.pop()

    def __repr__(self):
        for card in self.__deck:
            print(card)
        return ''

    def remove(self, index):
        self.__deck = [card for card in self.__deck if card.index != index]
        return self.__deck

    def __len__(self):
        return len(self.__deck)
