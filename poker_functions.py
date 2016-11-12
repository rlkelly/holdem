from models.card import Card
from models.deck import Deck
from models.dealer import Dealer
from models.player import Player
from models.pokertable import PokerTable
from models.hand import Hand
from models.defaultdict import DefaultDict


def create_deck_without_cards(cards, player1, player2, flop):
    deck = Deck()
    cards = flop[:]
    cards.extend(player1.hand)
    cards.extend(player2.hand)
    for card in cards:
        deck.remove(card.index)
    return deck


def finish_hand(community_cards, player1, player2, flop):
    flop_deck = create_deck_without_cards(community_cards, player1, player2, flop)
    flop_deck.shuffle()
    community = community_cards[:]
    while len(community) < 5:
        community.append(flop_deck.remove_top_card())
    return compare_hands([player1.hand, player2.hand], community)


def hand_checker(player_cards, table_cards):
    all_cards = []
    all_cards.extend(player_cards)
    all_cards.extend(table_cards)
    raw_hand = [card.raw_info() for card in all_cards]

    d = DefaultDict(1)
    for value in raw_hand:
        d += value[0]

    raw_values = d.sorted_values()

    straight_outcome, top_straight_card = straight_check(raw_values)
    flush_outcome, flush_cards = flush_check(raw_hand)

    count = sorted(d.counter(), key=lambda x: (-x[1], -x[0]))

    if flush_outcome and straight_outcome:
        # TODO: This will be wrong some of the time
        if top_straight_card in flush_cards:
            return 0, top_straight_card, top_straight_card - 1
            return 'STRAIGHT FLUSH: {}'.format(top_straight_card)
    if count[0][1] == 4:
        return 1, count[0][0], count[1][0]
        return 'FOUR OF A KIND: {}'.format(count[0][0])
    if count[0][1] == 3 and count[1][1] >= 2:
        return 2, count[0][0], count[1][0]
        return 'FULL HOUSE: {} {}'.format(count[0][0], count[1][0])
    if flush_outcome:
        return 3, flush_cards[0], flush_cards[1]
        return 'FLUSH: {}'.format(flush_cards[0])
    if straight_outcome:
        return 4, top_straight_card, top_straight_card - 1
        return 'STRAIGHT: {}'.format(top_straight_card)
    if count[0][1] == 3:
        return 5, count[0][0], count[1][0]
        return 'THREE OF A KIND: {}'.format(count[0][0])
    if count[0][1] == 2 and count[1][1] == 2:
        return 6, count[0][0], count[0][1]
        return 'TWO PAIR: {} {}'.format(count[0][0], count[1][0])
    if count[0][1] == 2:
        return 7, count[0][0], count[1][0]
        return 'PAIR: {}, HIGH CARD: {}'.format(count[0][0], count[1][0])
    else:
        return 8, count[0][0], count[1][0]
        return 'HIGH CARD {}'.format(count[0][0])


def compare_hands(hands, community):
    hand1, hand2 = hands
    first_hand = hand_checker(hand1, community)
    second_hand = hand_checker(hand2, community)
    if first_hand[0] > second_hand[0]:
        return 'SECOND HAND WINNER'
    if first_hand[0] < second_hand[0]:
        return 'FIRST HAND WINNER'
    if first_hand[1] < second_hand[1]:
        return 'SECOND HAND WINNER'
    if first_hand[1] > second_hand[1]:
        return 'FIRST HAND WINNER'
    if first_hand[2] > second_hand[2]:
        return 'FIRST HAND WINNER'
    if first_hand[2] < second_hand[2]:
        return 'SECOND HAND WINNER'
    return 'BETTOR WINS...'


def flush_check(hand):
    flush_suit = None
    raw_suits = [val[1] for val in hand]
    flush_dict = DefaultDict(1)
    for val in raw_suits:
        flush_dict += val
    for key in flush_dict.dict.keys():
        if flush_dict.dict[key] >= 5:
            flush_suit = key
    if flush_suit:
        flush_cards = [card[0] for card in hand if card[1] == flush_suit]
        return True, sorted(flush_cards, reverse=True)
    return None, None


def straight_check(hand):
    straight_pos, outcome = None, None
    straight_check = list(map(lambda x: x[0] - x[1], enumerate(hand)))

    d2 = DefaultDict(1)
    for val in straight_check:
        d2 += val
    for val in d2.dict:
        if d2.dict[val] >= 4:
            straight_pos = d2.dict[val]
            straight_value = val

    if straight_pos and straight_pos >= 4:
        first = [index for index, val in enumerate(straight_check) if val == straight_value]
        if first:
            if hand[first[-1]] == 4 and 13 in hand:
                # print('wheel')
                outcome = True, 4
            if straight_pos >= 5:
                # print('{} high straight'.format(hand[first[-1]]))
                outcome = True, hand[first[-1]]
    return None, None
