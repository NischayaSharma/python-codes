def mod(num):
    return -num if(num<0) else num;

def main():
    minDist = 999999;
    sum = 0;
    numOfMembers = input();
    locationOfAkatsuki = [];
    locationOfLeaf = [];
    for i in range(numOfMembers):
        locationOfAkatsuki.append(raw_input().split());
    for i in range(numOfMembers):
        locationOfLeaf.append(raw_input().split());
    for i in range(numOfMembers):
        minDist = 999999;
        for j in range(numOfMembers):
            xDiff = mod(int(locationOfAkatsuki[i][0])-int(locationOfLeaf[j][0]));
            yDiff = mod(int(locationOfAkatsuki[i][1])-int(locationOfLeaf[j][1]));
            dist = xDiff + yDiff;
            minDist = minDist if(minDist<dist) else dist;
            print i,j,dist,minDist;
        sum += minDist;
    print sum;

main();
