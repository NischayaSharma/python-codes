import sys;

length, wantedCandies = raw_input().split();
arr = raw_input().split();
for i in range(int(length)):
    for j in range(i+1,int(length)):
        if(int(arr[i])+ int(arr[j]) == int(wantedCandies)):
            print i+1,j+1;
            sys.exit();
