from ..library import strategyHelpers
from ..library import compareHands

def flattenState(boardState):

    return [
        card
        for player in boardState
        for col in player
        for card in col
    ]

def isOnForFlush(col):
    if(len(col)) == 0:
        return True
    suit = col[0][1]
    for card in col:
        if card[1] != suit:
            return False
    return True

def chooseGroup(card, myOptions, myCols):

    results = []
    for opt in myOptions:
        results.append( (opt, "".join(myCols[opt]).count(strategyHelpers.readCard(card)["val"]) ) )

    results = sorted(results, key=lambda x: (x[1]), reverse=True)
    filtered = []
    for result in results:
        if result[1] > 0:
            filtered.append(result)

    if len(filtered) == 0:
        return False

    return filtered[0][0]



def choose(boardState, card, turn):
    myCols = boardState[strategyHelpers.getPlayerNumberFromTurn(turn)]
    if strategyHelpers.isSwapRound(turn):
        myOptions = []
        for i in range(5):
            col = myCols[i]
            if strategyHelpers.isSwapAnImprovement(col, card):
                myOptions.append(i)
        if len(myOptions) == 0:
            return -1
        return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseFlush, strategyHelpers.chooseStraight, strategyHelpers.chooseGroup])

    myOptions = strategyHelpers.getMyOptions(boardState, turn)
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [chooseGroup, strategyHelpers.chooseFlush, strategyHelpers.chooseStraight])