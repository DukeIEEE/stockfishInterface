from moveFunctions import moveFunction
    
moveFcn = moveFunction()
moveList = ["e2e4", "f7f5", "e4f5"]


for move in moveList: 
    bestMoves = moveFcn.receiveMove()
    print "bestMove:" + bestMoves
    moveFcn.sendMove(move)

