from math import log
M = int(1e9+7)
t = int(input())
while t:
    a,b=map(int,input().split())
    if b==0:
        print(1)
        t-=1
        continue
    ans = 1
    x = a
    for i in range(0,int(log(b,2))+1):
        if b&1:
            ans=(ans*x)%M
        x=(x*x)%M
        b>>=1
    print(ans)
    t-=1
