from ..library import strategyHelpers


def choose(boardState, card, turn):
    myOptions = strategyHelpers.getMyOptions(boardState, turn)
    myCols = boardState[strategyHelpers.getPlayerNumberFromTurn(turn)]
    result = strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseGroup, strategyHelpers.chooseStraight, strategyHelpers.chooseFlush])
    if strategyHelpers.isSwapRound(turn):
        if not strategyHelpers.isSwapAnImprovement(myCols[result], card):
            return -1
    return result
