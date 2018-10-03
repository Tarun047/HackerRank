t = int(input())
while t:
    n = int(input())
    a = sorted(set([int(x) for x in input().split()]))
    b = [1 for _ in range(len(a))]
    for i in range(1,len(a)):
        if a[i]-a[i-1]==1:
            b[i]=b[i-1]+1
    d = max(b)
    print(d)
    t-=1
