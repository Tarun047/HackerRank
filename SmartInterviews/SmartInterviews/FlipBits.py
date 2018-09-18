t = int(input())
while t:
    a,b = map(int,input().split())
    ans = 0
    while a>0 or b>0:
        ans += (a&1)^(b&1)
        a>>=1
        b>>=1
    print(ans)
    t-=1
