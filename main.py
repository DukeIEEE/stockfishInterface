from subprocess import Popen, PIPE

exe_str = "stockfish-6-win\Windows\stockfish-6-64.exe"

blackMoves = ['h7h6', 'g7g6', 'e7e6'];
moves=[];

def getMoves():
    tempStr = '';
    for x in moves:
        tempStr += x + " ";
    return tempStr;

parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE); 

for x in blackMoves:
    parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE); 
    output = parent.communicate('go')
    moves.append(output[0].split()[-1])
    moves.append(x) 
    sendString = "position startmov moves %s" % getMoves();
    print sendString
    parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE); 
    parent.communicate(sendString);
    parent.wait()



print moves