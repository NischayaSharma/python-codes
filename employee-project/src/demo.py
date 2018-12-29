listOfDigit = [9,9,9,9,8,3]
for j in range(len(listOfDigit)):
    rotatingList = (listOfDigit[j:] + listOfDigit[:j]);
    print rotatingList;
# listOfPermutation = permutationOfNum(i);
# for j in range(len(listOfPermutation)):
#     listOfPermutation[j] = listToNum(listOfPermutation[j]);
# for k in range(len(listOfPermutation)):
#     if(not isPrime(listOfPermutation[k])):
#         isCircularPrime = False;
#         break;
