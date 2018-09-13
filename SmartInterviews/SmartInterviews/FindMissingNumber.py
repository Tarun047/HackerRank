t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in range(1,n+2)]
    b = [int(x) for x in input().split()]
    print(sum(a)-sum(b))
    t-=1
