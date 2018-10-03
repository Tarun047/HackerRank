from collections import Counter
    
n = int(input())
a = Counter([int(x) for x in input().split()])
q = int(input())
while q:
    print(a[int(input())])
    q-=1
