t = int(input())
j=1
while j<=t:
    n = int(input())
    print('Case #{}:'.format(j))
    ans = []
    for i in range(0,n//2+1):
        if i==0:
            ans.append(' '*(n//2-i)+'*')
        else:
            ans.append(' '*(n//2-i)+'*'+' '*(2*i-1)+'*')
    print('\n'.join(ans)+'\n'+'\n'.join(ans[::-1][1:]))
    j+=1
