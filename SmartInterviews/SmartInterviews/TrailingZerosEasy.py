from math import factorial
t = int(input())
while t:
    n = int(input())
    c = 0
    i = 1
    temp = n
    while temp>2**i:
        temp>>=1
        c+=temp
    temp = n
    i = 1
    c2 = 0
    while n>=5**i:
        c2+=(n//5**i)
        i+=1
    print(min(c,c2))
    t-=1
