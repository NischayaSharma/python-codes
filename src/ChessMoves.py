import sys;

def mod(num):
    return -num if(num<0) else num;

numOfTestCases = input();
column = 1;
row = 0;

for i in range(numOfTestCases):
    dimensionStr, rowWhite, colWhite, rowBlack, colBlack, moveStr = raw_input().split();
    dimension = int(dimensionStr);
    move = int(moveStr)
    coordBlack = [int(rowBlack), int(colBlack)];
    coordWhitePawn = [int(rowWhite), int(colWhite)];
    coordWhiteKing = [1,int(dimension)];

    draw = False;
    whiteWins = False;
    whiteMoves = dimension - coordWhitePawn[row];

    # Calculate moves for black after checking if row or column is closer.
    blackMoves = mod(coordWhitePawn[column]-coordBlack[column] if(mod(coordWhitePawn[column]-coordBlack[column]) < mod(dimension-coordBlack[row])) else dimension-coordBlack[row]);
    coordBlack[row] += blackMoves;
    if(coordBlack[column]>coordWhitePawn[column]):
        coordBlack[column] -= blackMoves;
    else:
        coordBlack[column] += blackMoves;
    print coordBlack;

    # If black has still not reached white's column in n-row then calculate moves/steps again.
    if(coordBlack[row]+coordBlack[column] != dimension+coordWhitePawn[column]):
        blackMoves = (mod(dimension-coordBlack[row]) if(mod(coordWhitePawn[column]-coordBlack[column]) < mod(dimension-coordBlack[row])) else mod(coordWhitePawn[column]-coordBlack[column])) + mod(blackMoves);

    blackMoves -= move;

    # Final - if no. of moves for black to target is lesser it indicates draw.
    if(blackMoves<=whiteMoves):
        print "Draw";
    else:
        print "White Wins";
