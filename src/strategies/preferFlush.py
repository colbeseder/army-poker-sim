def choose(board, card, turn):
    suit = card[1]
    iam = turn %2
    myCols = board.state[iam]
    minimumLength = min([len(col) for col in myCols])
    myOptions = []
    for i in range(5):
        if len(myCols[i]) == minimumLength:
            myOptions.append(i)
    for opt in myOptions:
        if "".join(myCols[opt]).count(suit) == minimumLength:
            return opt
    return myOptions[0]
