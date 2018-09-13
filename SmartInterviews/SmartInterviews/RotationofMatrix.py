t = int(input())
for p in range(t):
    print('Test Case #{}:'.format(p+1))
    n = int(input())
    a = [[int(x) for x in input().split()]for _ in range(n)]
    a = [[str(a[j][i]) for j in range(n)]for i in range(n)]
    a = list(map(reversed,a))
    for row in a:
        print(' '.join(row))
