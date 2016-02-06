import string

class gCode(object):
	xUnit = 1;
	yUnit = 1;


	def __init__(self):
		self.alphaNumericDi=dict(zip(string.letters,[ord(c)%32 for c in string.letters]));


	def getParsedMoves(self,command):
		#handles casting and regular moves
		move = [command]
		if(command=='e1g1'): #castling white right side
			move.append('h1f1');

		return move;



	def getgCodeFromMove(self,arr):
		fullString = ""
		for k in range(0,arr.length):
			move = arr[k];
			move1 = move[:2];
			move2 = move[2:];

			str1 = getGCode(move1);
			str2 = getGCode(move2);
			fullString = fullString + " " + str1 + " " + str2;
		end
		return fullString;

	def getGCode(self,move):
		xDist = self.di[move[0]]*xUnit;
		yDist = int(move[1])*yUnit;

		xStr = "X" + str(xDist);
		yStr = "Y" + str(yDist);
		fullStr = "G00" + " " + xStr + " " + yStr + "\n";

		return fullStr;