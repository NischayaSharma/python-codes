# import math as mt;
#
# def fibonacci(num):
#     phi = (mt.sqrt(5)+1.00)/2.00;
#     return ((phi**num)-((-phi)**(-num)))/mt.sqrt(5);
#
# def numOfDigits(num):
#     numOfDigits = 0;
#     while (num>0):
#         num = num/10;
#         numOfDigits += 1;
#     return numOfDigits;
#
# def main():
#     n=0;
#     while(n>=0):
#         fib = fibonacci(n);
#         num = numOfDigits(fibonacci(n));
#         print n,"\t",fib;
#         if(num>=1000):
#             break;
#         n+=1;
#     print "answer:",n;
# main();
def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

for index, number in enumerate(fibo()):
    if len(str(number)) == 1000:
        print(index)
        break
