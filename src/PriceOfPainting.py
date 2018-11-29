numOfTestCases=input();
numOfHouses=input();
for i in range (numOfTestCases):
    min=0;
    sum=0;
    pink = False;
    orange = False;
    yellow = False;
    pinkCounter=0;
    orangeCounter=0;
    yellowCounter=0;
    for j in range(numOfHouses):
        priceOfPink, priceOfOrange, priceOfYellow = raw_input().split();
        min = int(priceOfYellow if(priceOfYellow<priceOfOrange and priceOfYellow<priceOfPink) else priceOfOrange if(priceOfOrange<priceOfYellow and priceOfOrange<priceOfPink) else priceOfPink);
        if(pink):
            min = int(priceOfYellow if(priceOfYellow<priceOfOrange) else priceOfOrange);
        if(orange):
            min = int(priceOfPink if(priceOfYellow>priceOfPink) else priceOfYellow);
        if(yellow):
            min = int(priceOfOrange if(priceOfPink>priceOfOrange) else priceOfPink);
        sum+=min;
        print(min);
        if(min==int(priceOfPink) and not pink):
            pink=True;
        elif(min==int(priceOfOrange) and not orange):
            orange=True;
        elif(min==int(priceOfYellow) and not yellow):
            yellow=True;
        print pink,orange,yellow;
    print sum;
