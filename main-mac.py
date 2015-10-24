import pexpect
addr = 'stockfish-6-mac/Mac/stockfish-6-64'

child = pexpect.spawn(addr)

child.sendline('uci')
child.sendline('go')
child.expect_exact("ponder ")

print child.before
print ("\n\n")

child.sendline("position startpos moves g1f3")
child.sendline("go")
child.expect_exact("ponder ")

print child.before
print ("\n\n")

child.sendline("position startpos moves g1f3 d7d5")
child.sendline("go")
child.expect_exact("ponder ")

print child.before



