from gCodeParse import *

lol = gCode();


hello = lol.getgCodeFromMove(lol.getParsedMoves('e1g1'));
print hello;