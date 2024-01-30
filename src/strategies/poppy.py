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
    suit = col[0][1]
    for card in col:
        if card[1] != suit:
            return False
    return True

def chooseGroup(card, myOptions, myCols):
    best = False
    for opt in myOptions:
        # Groups
        if strategyHelpers.readCard(card)["val"] in "".join(myCols[opt]):
            best = opt
            if not isOnForFlush(myCols[opt]):
                return opt
    return best



def choose(boardState, card, turn):
    myCols = boardState[strategyHelpers.getPlayerNumberFromTurn(turn)]
    if turn > 50: # Swap turn
        myOptions = []
        for i in range(5):
            col = myCols[i]
            if compareHands.getWinner(''.join(col), ''.join(col[:4] + [card])) == -1:
                myOptions.append(i)
        if len(myOptions) == 0:
            return -1
        return strategyHelpers.chooseByPriority(card, myOptions, myCols, [chooseGroup, strategyHelpers.chooseFlush, strategyHelpers.chooseStraight])
    
    myOptions = strategyHelpers.getMyOptions(boardState, turn)
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [chooseGroup, strategyHelpers.chooseFlush, strategyHelpers.chooseStraight])