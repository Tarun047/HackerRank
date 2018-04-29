import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static boolean isPallindrome(int n)
    {
        int temp = n,r=0,d;
        while(temp>0)
        {
            d = temp%10;
            r=r*10+d;
            temp/=10;
        }
        if(n==r)
            return true;
        else
            return false;
    }
    public static boolean isProduct(int n)
    {
        int i;
        for(i=(int)Math.sqrt(n);i>=100;i--)
            if(n%i==0 && n/(i*1000)==0)
                return true;
        return false;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while(t>0){
        int n = in.nextInt();
        while(!isPallindrome(n) || !isProduct(n))
        {
            n--;
        }
        System.out.println(n);
        t-=1;
      }
    }
}
