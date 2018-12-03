upStr, downStr, targetStr = raw_input().split();
up = long(upStr);
down = long(downStr);
target = long(targetStr);
counter = 0;
dailySteps = up-down;
counter = (target-up) / dailySteps;

if((target-up) % dailySteps > 0):
    counter += 1;
print counter+1;
