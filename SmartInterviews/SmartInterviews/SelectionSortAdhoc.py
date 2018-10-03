t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = []
    for i in range(0,n-1):
        m = n-i-1
        for j in range(0,n-i-1):
            if a[m]<=a[j]:
                if a[m]==a[j] and j>m:
                    continue
                m=j
        ans.append(m)
        a[n-i-1],a[m]=a[m],a[n-i-1]
            
    print(" ".join(list(map(str,ans))))
    t-=1
