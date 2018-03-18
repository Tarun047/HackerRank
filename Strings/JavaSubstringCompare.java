import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest = s.substring(0,k);
        int n=s.length();
       for(int i=0;i<=n-k;i++)
        {
            String t=s.substring(i,i+k);    
            smallest=smallest.compareTo(t)>0?t:smallest;
            largest=largest.compareTo(t)>0?largest:t;
       }
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
