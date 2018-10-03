def towersOfHanoi(n,src,temp,dest):
    if n==0:
        return
    towersOfHanoi(n-1,src,dest,temp)
    print("Move {0} from {1} to {2}".format(n,src,dest))
    towersOfHanoi(n-1,temp,src,dest)
t=int(input())
while t:
    n=int(input())
    print((1<<n)-1)
    towersOfHanoi(n,"A","B","C")
    t-=1
