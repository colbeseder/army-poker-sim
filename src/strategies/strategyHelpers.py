def getPlayerNumberFromTurn(turn):
    return turn % 2


def readCard(card):
    return {
        "val" : card[0],
        "suit": card[1]
    }


def getMyOptions(board, turn):
    myCols = board.state[getPlayerNumberFromTurn(turn)]
    minimumLength = min([len(col) for col in myCols])
    myOptions = []
    for i in range(5):
        if len(myCols[i]) == minimumLength:
            myOptions.append(i)
    return myOptions


def chooseFlush(card, myOptions, myCols):
    for opt in myOptions:
        if "".join(myCols[opt]).count(readCard(card)["suit"]) == len(myCols[opt]):
            return opt
    return False


cardValOrder = "A23456789TJQKA"
def getValIndex(a):
    return cardValOrder.index(a)


def chooseStraight(card, myOptions, myCols):
    for opt in myOptions:
        cardValues = [readCard(c)["val"] for c in myCols[opt]]
        cardValues.sort(key=getValIndex)
        if "".join(cardValues) in cardValOrder:
            return opt
    return False


def chooseGroup(card, myOptions, myCols):
    for opt in myOptions:
        # Groups
        if readCard(card)["val"] in "".join(myCols[opt]):
            return opt
    return False


def chooseByPriority(card, myOptions, myCols, choiceFuncs):
    for func in choiceFuncs:
        result = func(card, myOptions, myCols)
        if result is not False:
            return result
    return myOptions[0]
