#SetBit Based Solution - Efficient Approach
def getSetBits(n):
    c = 0
    while(n>0):
        n=n&(n-1)
        c+=1
        if(c>1):
            return False
    return True
t = int(input())
while t:
    print(getSetBits(int(input())))
    t-=1
