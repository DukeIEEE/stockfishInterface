import wexpect


def getbest(stockfishoutput):
    stockfisharray = stockfishoutput.split(" ")
    bestmove = stockfisharray[len(stockfisharray)-2]
    return bestmove


addr = "stockfish-6-win\Windows\stockfish-6-64.exe"
command = "position startpos moves"
moveList = ["g7g6", "a7a5", "h7h5", "g8f6"]

child = wexpect.spawn(addr)
child.sendline('uci')

for i in range(0, len(moveList)):
    child.sendline('go')
    child.expect_exact("ponder ")
    bestmove = getbest(child.before)
    print("Computer's move: " + bestmove + "\n")
    #add computer move
    command += (" " + bestmove)
    print "Command: "+ command + "\n"

    #add person move
    command += (" " + moveList[i])
    print("Person's move: " + moveList[i] + "\n")
    print "Command: " + command + "\n"
    child.sendline(command)