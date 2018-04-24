#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = 0
    p = (n-1)//3
    q = (n-1)//5
    r = (n-1)//15
    if(p!=1):
        s+=(p*3*(1+p))//2
    else:
        s+=3
    if(q!=1):
        s+=(q*5*(1+q))//2
    else:
        s+=5
    if(r==0):
        print(s)
    else:
        s-=(r*15*(1+r))//2
        print(s)
