t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    s = 0
    for i in range(0,n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                s+=1
    print(s)
    t-=1
