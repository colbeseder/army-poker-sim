from . import compareHands


class Board():
    def __init__(self):
        self.deck = Deck()
        self.state = [
            [ 5* []],
            [ 5 * []]
        ]

    def add(self, player, column, card): # player 0 or 1
        if player not in [0, 1]:
            raise Exception("invalid player %s" %[player])
        if column not in range(5):
            raise Exception("invalid column %s" %[column])
        minimum_length = min([len(col) for col in self.state[player]])
        if len(self.state[player][column]) > minimum_length:
            raise Exception("Can't add card to column %s as it's not the shortest" % [column])
        self.state[player][column] += card

    def swap(self, player, column, card):
        self.state[player][column][-1] = card

    def getPreparedColsForCompare(self):
        pairs = []
        for col in range(5):
            pairs += (
                " ".join(self.state[0][col]),
                " ".join(self.state[1][col]),
            )
        return pairs

    def getResult(self):
        pairs = self.getPreparedColsForCompare()
        score = 0
        for pair in pairs:
            score += compareHands.getWinner(pair[0], pair[1])
        return score
