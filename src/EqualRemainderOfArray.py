n=input();
max=0;
arr = range(n);
arrRem = range(n);
isEqual=True;
for i in range(n):
    arr[i]=input();
    max = max if(max>arr[i]) else arr[i];
for i in range(max):
    isEqual=True;
    for j in range(n):
        if(i!=0):
            arrRem[j] = arr[j]%i;
    #print arrRem,i;
    for k in range(n-1):
        if(arrRem[k]!=arrRem[k+1]):
            isEqual=False;
    if(isEqual and i!=1):
        print i,;
