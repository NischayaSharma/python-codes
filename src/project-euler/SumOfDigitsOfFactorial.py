def factorial(num):
    print "Inside factorial",num;
    if(num==1):
        return 1;
    return num*factorial(num-1);

def sumOfDigits(num):
    sumOfDig = 0;
    while (num>0):
        print "Inside sumOfDigits",num;
        sumOfDig += (num%10);
        num = num//10;
    return sumOfDig;
def main():
    fact = factorial(100);
    print fact;
    sum = sumOfDigits(fact);
    print "Sum of digits of",fact,"is",sum;

main()
