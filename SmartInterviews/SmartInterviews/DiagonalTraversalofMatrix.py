t = int(input())
ans = []
while t:
    x = []
    n = int(input())
    a = [[int(x) for x in input().split()]for _ in range(n)]
    for k in range(n-1,0,-1):
        s = 0
        for i,j in zip(range(0,n),range(k,n)):
            s+=a[i][j]
        x.append(str(s))
    x.append(str(sum(a[i][i] for i in range(n))))
    for k in range(1,n):
        s = 0
        for i,j in zip(range(k,n),range(0,n)):
            s+=a[i][j]
        x.append(str(s))
    ans.append(' '.join(x))
    t-=1
print('\n'.join(ans))
