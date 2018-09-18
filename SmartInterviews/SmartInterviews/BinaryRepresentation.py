from math import log
t = int(input())
while t:
    n = int(input())
    if n==0:
        print(0)
        t-=1
        continue
    ans = []
    for i in range(0,int(log(n,2))+1):
        ans += str(n&1)
        n>>=1
    print(''.join(reversed(ans)))
    t-=1
