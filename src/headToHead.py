import math
from .library import Game


def head2Head(strategy1, strategy2, iterations=1000):
    score = 0
    for i in range(int(iterations/2)):
        game = Game.Game(strategy1, strategy2)
        result = game.result
        if result > 0:
            score += 1
        elif result < 0:
            score -= 1
        last = i
    # Swap player1 & Player2
    for i in range(last+1, iterations):
        game = Game.Game(strategy2, strategy1)
        result = game.result
        if result > 0:
            score -= 1
        elif result < 0:
            score += 1

    return score


if __name__ == "__main__":

    from .strategies import chooseLeft, preferGroupFlushStraight, preferGroupStraightFlush, preferGroups


    strategy1 = preferGroupFlushStraight
    strategy2 = preferGroupStraightFlush
    iterations = 10000
    score = head2Head(strategy1, strategy2, iterations)

    if score > 0:
        winner = "Strategy 1 (%s)" % (strategy1.__name__)
    elif score < 0:
        winner = "Strategy 2 (%s)" % (strategy2.__name__)
    else:
        print("It's a Draw!!")
        exit()


    print("%s won, with a difference of %s out of %s games (%s%%)" % (winner, abs(score), iterations, math.floor((abs(score)/iterations)*100)))
