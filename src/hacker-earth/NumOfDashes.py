numOfDashes = {0:6, 1:2, 2:5, 3:5, 4:4, 5:6, 6:6, 7:3, 8:7, 9:6};
num = int(input());
sumOfDashes = 0;
while(num>0):
    sumOfDashes += numOfDashes[num%10];
    num = num//10;
print (sumOfDashes);
