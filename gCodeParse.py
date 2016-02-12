import string


class gCode(object):
    def __init__(self):
        self.xUnit = 1;
        self.yUnit = 1;
        self.alphaNumericDi = dict(zip(string.letters, [ord(c) % 32 for c in string.letters]));

    def getParsedMoves(self, command):
        # handles casting and regular moves
        move = [command]
        if (command == 'e1g1'):  # castling white right side
            move.append('h1f1');
        elif(command == 'e1b1'):
            move.append('a1c1');
        elif(command == 'e8g8'):
            move.append('h8f8');
        elif(command == 'e8b8'):
            move.append('a8c8');
        return move;

    def getgCodeFromMove(self, arr):
        fullString = "";
        for move in arr:
            move1 = move[:2];
            move2 = move[2:];

            str1 = self.getGCode(move1);
            str2 = self.getGCode(move2);
            fullString = fullString + str1 + str2;

        return fullString;

    def getGCode(self, move):
        xDist = self.alphaNumericDi[move[0]] * self.xUnit;
        yDist = int(move[1]) * self.yUnit;

        xStr = "X" + str(xDist);
        yStr = "Y" + str(yDist);
        fullStr = "G00" + " " + xStr + " " + yStr + "\n";

        return fullStr;
