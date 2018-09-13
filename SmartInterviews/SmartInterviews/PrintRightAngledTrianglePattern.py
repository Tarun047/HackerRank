t = int(input())
j = 1
while j<=t:
    print('Case #{}:'.format(j))
    n = int(input())
    for i in range(n):
        print(' '*(n-1-i)+'*'*(i+1))
    j+=1
