from poker_functions import finish_hand
from models.dealer import Dealer
from models.player import Player
from models.pokertable import PokerTable


def main():
    dealer = Dealer('Floyd', PokerTable(2))
    dealer.shuffle_deck()
    player1 = Player('Abbott')
    player2 = Player('Costello')

    dealer.seat_player(player1)
    dealer.seat_player(player2)

    dealer.deal_cards()
    flop = dealer.flop()[:]
    second_hand, first_hand, tie = 0, 0, 0

    print 'First Player Hand: %s' % player1.hand
    print 'Second Player Hand: %s' % player2.hand
    print 'Flop: %s' % flop


    for _ in range(100):
        results = finish_hand(flop, player1, player2, flop)
        if results == 'SECOND HAND WINNER':
            second_hand += 1
        elif results == 'FIRST HAND WINNER':
            first_hand += 1
        else:
            tie += 1

    return first_hand, second_hand, tie


if __name__ == '__main__':
    first, second = 0, 0
    for _ in range(10):
        first, second, bluff = main()

        print 'player 1 wins: %s' % first
        print 'player 2 wins: %s'% second
        print 'bluffer wins: %s' % bluff
        print
