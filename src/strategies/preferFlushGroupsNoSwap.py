from ..library import strategyHelpers


def choose(boardState, card, turn):
    if strategyHelpers.isSwapRound(turn):
        return -1
    myOptions = strategyHelpers.getMyOptions(boardState, turn)
    myCols = boardState[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseFlush, strategyHelpers.chooseGroup])