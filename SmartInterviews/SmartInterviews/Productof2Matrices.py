t = int(input())
while t:
    m1,n1 = map(int,input().split())
    a = [[int(x) for x in input().split()]for _ in range(m1)]
    m2,n2 = map(int,input().split())
    b = [[int(x) for x in input().split()]for _ in range(m2)]
    c = [[0 for _ in range(n2)]for _ in range(m1)]
    for i in range(0,m1):
        for j in range(0,n2):
            for k in range(0,n1):
                c[i][j]+=(a[i][k]*b[k][j])
    for row in c:
        print(' '.join(list(map(str,row))))
