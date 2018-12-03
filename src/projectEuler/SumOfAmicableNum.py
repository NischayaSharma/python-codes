
def isAmicable(num):
    sumOfDivisor = 0;
    sumOfSumOfDivisor = 0;
    for i in range(1,(num/2)+1):
        if num%i==0:
            sumOfDivisor+=i;
    for j in range(1,(sumOfDivisor/2)+1):
        if sumOfDivisor%j==0:
            sumOfSumOfDivisor+=j;
    if (sumOfDivisor==num):
        return False;
    return sumOfSumOfDivisor==num;

def main():
    sum = 0;
    for i in range (1,10001):
        if isAmicable(i):
            sum+=i;
            print i,"\t",sum;

main();
