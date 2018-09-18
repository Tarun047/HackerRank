from math import log
t = int(input())
while t:
    a = int(input())
    if(a==0):
        print(0)
        t-=1
        continue
    x = 1
    ans = 0
    for i in range(0,int(log(a,2))+2,2):
        t1 = a&1 #Check last bit
        t2 = a>>1&1 #Check last but one bit
        if t2: #If last but one bit is set update the ans with the current power of two
            ans += x
        if t1: #If last bit is set update the ans with the next power of two
            ans += x*2
        x=x*4 #Go by steps of 2**2 = 4 in each iteration as we swap 2 bits at a time
        a>>=2
    print(ans)
    t-=1
