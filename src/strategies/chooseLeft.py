import math

def choose(board, card, turn):
    choice = math.floor(turn / 2) % 5
    return choice
