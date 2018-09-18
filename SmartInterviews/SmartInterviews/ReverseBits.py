from math import log
t = int(input())
while t:
    n = int(input())
    ans = 0
    if n==0:
        t-=1
        print(0)
        continue
    for i in range(0,int(log(n,2))+1):
        if n&1:
            ans += 1<<(32-i-1)
        n>>=1
    print(ans)
    t-=1
