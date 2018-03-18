import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Solution{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}
class MyRegex{
/* 
 \d - To represent a digit
 \d{1,2} - All 1 digit and 2 digit Numbers 
 (0|1)\d{2} - All 3 digit Numbers beggining with 0 or 1
 2[0-4]\d - 20 to 24 numbers followed by a single digit
            ie. 200 to 249 Numbers
 25[0-5] - 250 to 255 Numbers 
*/
String z = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])";
String pattern = z + "." + z +"." +z +"." + z;
}