#Spiral Traversal of Matrix Source Code
t = int(input())
while t:
    n = int(input())
    a = [[int(x) for x in input().split()]for _ in range(n)]
    #r - row, c-column, ub-upperbound, lb-lowerbound
    rub = n-1
    cub = n-1
    rlb = 0
    clb=0
    k = 0
    ans = []
    while k<n//2+1:
        for j in range(rlb,rub):
            ans.append(str(a[rlb][j]))
        for i in range(clb,cub):
            ans.append(str(a[i][cub]))
        for j in range(rub,rlb,-1):
            ans.append(str(a[rub][j]))
        for i in range(cub,clb,-1):
            ans.append(str(a[i][clb]))
        rlb+=1
        clb+=1
        rub-=1
        cub-=1
        k+=1
    if(n%2!=0): #For odd nxn append center element to the answer
        ans.append(str(a[n//2][n//2]))
    t-=1
    print(" ".join(ans))
