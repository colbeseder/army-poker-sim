def choose(board, card, turn):
    val = card[0]
    iam = turn %2
    myCols = board.state[iam]
    minimumLength = min([len(col) for col in myCols])
    myOptions = []
    for i in range(5):
        if len(myCols[i]) == minimumLength:
            myOptions.append(i)
    for opt in myOptions:
        if val in "".join(myCols[opt]):
            return opt
    return myOptions[0]
