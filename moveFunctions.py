import pexpect

class moveFunction(object):
    def __init__(self):
        self.addr = '/home/pi/Desktop/stockfishInterface/stockfish'
        #self.addr = 'stockfish-6-mac/Mac/stockfish-6-64'
        self.moveCommand = "position startpos moves"
        self.moveString = ""
        self.child=pexpect.spawn(self.addr)
        self.child.sendline("uci")

    #Receives the move from the Chess Engine and sends it to the interface
    def receiveMove(self):
        self.child.sendline("go")
        self.child.expect_exact("ponder ")
        bestMove = self.getBest(self.child.before)
        self.moveString += (" " + bestMove)
        print 'moveString: ' + self.moveString + "\n"
        return bestMove

    #Sends the move the player made to the Engine
    def sendMove(self, nextMove):
        command = self.moveCommand + self.moveString + " " + nextMove
        self.child.sendline(command)
        self.moveString += (" " + nextMove)

    #Parses the output of the StockFish Engine and returns the BestMove
    def getBest(self, stockfishoutput):
        stockfisharray = stockfishoutput.split(" ")
        bestmove = stockfisharray[len(stockfisharray)-2]
        return bestmove
