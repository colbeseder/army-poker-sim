from . import strategyHelpers


def preferLeft(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [])


def preferFlush(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseFlush])


def preferGroup(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseGroup])

def preferStraight(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseStraight])

def preferGroupStraightFlush(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseGroup, strategyHelpers.chooseStraight, strategyHelpers.chooseFlush])

def preferGroupFlushStraight(board, card, turn):
    myOptions = strategyHelpers.getMyOptions(board, turn)
    myCols = board.state[strategyHelpers.getPlayerNumberFromTurn(turn)]
    return strategyHelpers.chooseByPriority(card, myOptions, myCols, [strategyHelpers.chooseGroup, strategyHelpers.chooseFlush, strategyHelpers.chooseStraight])