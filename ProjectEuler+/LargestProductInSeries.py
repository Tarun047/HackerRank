#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    b = []
    maxp=0
    for i in range(0,n-k+1):
        p = 1
        for j in num[i:i+k]:
            p = p * int(j)
        if(p>maxp):
            maxp = p
    print(maxp)
            
    
