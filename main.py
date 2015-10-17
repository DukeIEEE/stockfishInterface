from subprocess import Popen, PIPE
import time
exe_str = "stockfish-6-win\Windows\stockfish-6-64.exe"

blackMoves = ['h7h6', 'g7g6', 'e7e6'];
moves=[];

def getMoves():
    tempStr = '';
    for x in moves:
        tempStr += x + " ";
    return tempStr;

parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE); 
parent.stdout.flush()

for x in blackMoves:
    parent.stdin.write('go')
    output = parent.stdout.readline()
    print output
    moves.append(output.split()[-1])
    moves.append(x) 
    sendString = "position startmov moves %s" % getMoves();
    print sendString
    parent.stdin.write(sendString);



print moves