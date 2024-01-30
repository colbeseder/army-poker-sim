from . import compareHands

import random


class Deck():
    allCards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH',
                'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
                'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D', 'AD',
                'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S', 'AS']

    def __init__(self) -> None:
        self._cards = random.sample(self.allCards,len(self.allCards))

    def next(self):
        return self._cards.pop()


class Board():
    def __init__(self):
        self.deck = Deck()
        self.state = [
            [[] for _ in range(5)],
            [[] for _ in range(5)]
        ]

    # Hide last card in opponents columns
    def getSanitizedState(self, player):
        sanitizedState = [
            [ar.copy() for ar in self.state[0]],
            [ar.copy() for ar in self.state[1]]
            ]
        otherPlayer = (player + 1) % 2
        for col in sanitizedState[otherPlayer]:
            if len(col) == 5:
                col[4] = "??"
        return sanitizedState

    def add(self, player, column, card): # player 0 or 1
        if player not in [0, 1]:
            raise Exception("invalid player %s" %[player])
        if column not in range(5):
            raise Exception("invalid column %s" %[column])
        minimum_length = min([len(col) for col in self.state[player]])
        if len(self.state[player][column]) > minimum_length:
            raise Exception("Can't add card to column %s as it's not the shortest" % [column])
        self.state[player][column].append(card)


    def swap(self, player, column, card):
        self.state[player][column][-1] = card

    def getPreparedColsForCompare(self):
        pairs = []
        for col in range(5):
            pairs.append(
                (" ".join(self.state[0][col]),
                " ".join(self.state[1][col]))
            )
        return pairs

    def getResult(self):
        pairs = self.getPreparedColsForCompare()
        score = 0
        for pair in pairs:
            score += compareHands.getWinner(pair[0], pair[1])
        return score


class Game():
    def __init__(self, strat1, strat2) -> None:
        self._deck = Deck()
        self._board = Board()
        for turn in range(0, 50, 2): #TODO - Swapping round
            cardA = self._deck.next()
            colA = strat1.choose(self._board.getSanitizedState(0), cardA, turn)
            self._board.add(0, colA, cardA)

            cardB = self._deck.next()
            colB = strat2.choose(self._board.getSanitizedState(1), cardB, turn+1)
            self._board.add(1, colB, cardB)

        self.result = self._board.getResult()    
