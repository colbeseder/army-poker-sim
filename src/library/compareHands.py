""" Project 54 complete. Result: 376 """

import re

"""
1* - High Card: Highest value card.
2* - One Pair: Two cards of the same value.
3* - Two Pairs: Two different pairs.
4* - Three of a Kind: Three cards of the same value.
5* - Straight: All cards are consecutive values.
6* - Flush: All cards of the same suit.
7* - Full House: Three of a kind and a pair.
8* - Four of a Kind: Four cards of the same value.
9* - Straight Flush: All cards are consecutive values of same suit.
"""


def rank(hand):
    """ takes string, eg. '8C TS KC 9H 4S'. N.B. "10" is always represented by "T"
    Returns parsed array of integers. Hands can be compared by comparing these arrays.
    The hand with the highest value in the first column wins.
    If these are equal, the next column is compared, and so on.
    If the final column is equal, the hand is a draw. No arrays will not run out of columns before winning/losing except in a draw (i.e. identical arrays)
    The first column represents the type of hand (full house, pair, high card etc) - see chart
    The next columns represent the relevant cards (for full house, threes then twos), followed by the entire hand, from highest to lowest.
    """
    def replaceLetter(letter):  # returns number value of card
        dic = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
        if letter in dic:
            return dic[letter]
        return int(letter)

    def straight(vals):  # returns parsed array or false
        if vals[0] == 14 and vals[1] == 5:  # possible low Ace straight
            return straight(vals[1:5] + [1])
        for i in range(0, 4):
            if vals[i] != 1 + vals[i+1]:
                return False
        return [5] + vals

    def ofAKind(vals):
        groups = {}
        for i in range(0, 5):
            if vals[i] in groups:
                groups[vals[i]] += 1
            else:
                groups[vals[i]] = 1
        pairs = []
        three = 0

        for group in groups:
            val = groups[group]
            if val == 4:
                return [8, group] + vals  # 4 OAK
            if val == 2:
                pairs = [group] + pairs
            if val == 3:
                three = group

        if len(pairs):
            if three:
                return [7, three, pairs[0]] + vals  # Full House
            return ([(len(pairs) + 1)] + pairs) + vals  # 1pair / 2pairs
        if three:
            return [4, three] + vals  # 3 OAK
        return [1] + vals  # High Card

    suits = re.findall("[CSHD]", hand)
    flush = suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]
    vals = re.findall(r"[TJQKA\d]", hand)
    vals = sorted(map(replaceLetter, vals))
    straight_output = straight(vals)
    if straight_output:
        if flush:  # straight flush
            straight_output[0] = 9
            return straight_output
        else:  # straight
            return straight_output
    if flush:
        return [6] + vals  # regular flush

    return ofAKind(vals)


def getWinner(pl1, pl2):  # takes two hands. Returns Bool for if pl1 beats pl2. Draw returns False.
    hand1 = rank(pl1)
    hand2 = rank(pl2)

    for i in range(0, len(hand1)):
        if hand1[i] > hand2[i]:
            return 1
        if hand1[i] < hand2[i]:
            return -1
    return 0 #draw


def hand(str):
    # example hand: "8C TS KC 9H 4S 7D 2S 5D 3S AC"
    pl1 = str[0:14]
    pl2 = str[15:29]
    return getWinner(pl1, pl2)
