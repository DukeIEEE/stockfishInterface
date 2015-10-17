from subprocess import Popen, PIPE
exe_str = "stockfish-6-win\Windows\stockfish-6-64.exe"


parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE); 
output2 = parent.communicate('go')
print output2[0]
parent = Popen(exe_str,  stderr=PIPE, stdin=PIPE, stdout=PIPE);
output= parent.communicate('uci')
print output[0]

