
def isAbundant(num):
    sumOfDivisor=0;
    for i in range(1,(num//2)+1):
        if num%i==0:
            sumOfDivisor+=i;
            print "\nnum:",num,"\ti:",i;
    return sumOfDivisor>num;

def main():
    summation=0;
    for sum in range(1,28124):
        canBeWritten = False;
        for i in range(1,sum):
            print "i in main:",i,"sum:",sum;
            print "isAbundant(sum-i):",isAbundant(sum-i),"isAbundant(i):",isAbundant(i);
            sumMinusI=isAbundant(sum-i);
            abundantI=isAbundant(i);
            if(sumMinusI and abundantI):
                canBeWritten = True;
        print "canBeWritten:",canBeWritten;
        if(not canBeWritten):
            summation += sum;
    print summation;

main();
