from ..library import strategyHelpers


def choose(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseFlush, strategyHelpers.chooseGroup])