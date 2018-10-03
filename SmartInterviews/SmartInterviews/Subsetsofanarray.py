from itertools import combinations
t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = []
    for i in range(1,n+1):
        for comb in combinations(a,i):
            ans.append(sorted(comb))
    for comb in sorted(ans):
        print(' '.join(list(map(str,comb))))
    print('')
    t-=1
