from models.deck import Deck


class Dealer(object):

    def __init__(self, name, table):
        self.name = name
        self.deck = Deck()
        self.table = table
        self.muck = []
        self.community_cards = []

    def _shuffle(self, cut_card=26):
        self.deck.shuffle()

    def spread_deck(self):
        print(self.deck)

    def shuffle_deck(self):
        for _ in range(8):
            self._shuffle()

    def seat_player(self, player):
        self.table.seat_player(player)

    def deal_cards(self):
        for _ in range(2):
            for player in self.table.players:
                player.receive_card(self.deck.remove_top_card())

    def deal_hand(self):
        self.muck.append(self.deck.remove_top_card())
        for _ in range(3):
            self.community_cards.append(self.deck.remove_top_card())
        self.muck.append(self.deck.remove_top_card())
        self.community_cards.append(self.deck.remove_top_card())
        self.muck.append(self.deck.remove_top_card())
        self.community_cards.append(self.deck.remove_top_card())

    def next_card(self):
        self.muck.append(self.deck.remove_top_card())
        self.community_cards.append(self.deck.remove_top_card())

    def flop(self):
        self.muck.append(self.deck.remove_top_card())
        for _ in range(3):
            self.community_cards.append(self.deck.remove_top_card())
        return self.community_cards[:]

    def showdown(self):
        print(self.community_cards)
        print('')
        for player in self.table.players:
            print('%s: %s' %(player.name, player.hand))

    def compare_hands(self, hand1, hand2):
        pass
