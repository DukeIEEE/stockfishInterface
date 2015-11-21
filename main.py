from moveFunctions import moveFunction
    
moveFcn = moveFunction()
moveList = ["g7g6", "a7a5", "h7h5", "g8f6"]


for move in moveList: 
    bestMoves = moveFcn.receiveMove()
    print "bestMove:" + bestMoves
    moveFcn.sendMove(move)

