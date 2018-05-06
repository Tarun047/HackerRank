#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int lcm(int a,int b)
{
    return (a*b)/gcd(a,b);
}
int main(){
    int t,ans; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
    int n;
    scanf("%d",&n);
    if(n==1)
    {
        printf("1\n");
        continue;
    }
    if(n==2)
    {
        printf("2\n");
        continue;
    }
    ans = lcm(1,2);
    for(int i=3;i<=n;i++)
        ans = lcm(ans,i);
    printf("%d\n",ans);
        
    }
    return 0;
}
