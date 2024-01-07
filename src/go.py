import math

from library import Game
from strategies import chooseLeft, preferGroups, preferFlush, preferFlushGroups, preferGroupsFlush

score = 0

strategy1 = preferFlushGroups
strategy2 = preferGroupsFlush

howManyGames = 10000

for i in range(howManyGames):
    game = Game.Game(strategy1, strategy2)
    result = game.result
    if result > 0:
        score += 1
    elif result < 0:
        score -= 1

if score > 0:
    winner = "Strategy 1 (%s)" % (strategy1.__name__)
elif score < 0:
    winner = "Strategy 2 (%s)" % (strategy2.__name__)
else:
    print("It's a Draw!!")
    exit()


print("%s won, with a score of %s out of %s games (%s%%)" % (winner, abs(score), howManyGames, math.floor((abs(score)/howManyGames)*100)))
