from math import ceil,log
M = int(1e9+7)
def findQuadraticRoots(n):
    return (-1+(1+8*n)**0.5)/2
def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    ans = 1
    x = a
    for i in range(0,int(log(b,2))+1):
        if b&1:
            ans=(ans*x)%M
        x=(x*x)%M
        b>>=1
    return ans

t = int(input())


while t:
    n = int(input())
    i = ceil(findQuadraticRoots(n))
    p=i-1
    r = (p*(p+1)//2)
    #print(n,i,r)
    a = power(2,i)%M
    b = power(2,n-r-1)%M
    print((a+b)%M)
    t-=1
