class PokerTable(object):
    def __init__(self, seats):
        self.seats = seats
        self.players = []

    def seat_player(self, player):
        self.players.append(player)

    def player_gets_up(self, player):
        self.players = list(filter(lambda x: x!= player, self.players))
