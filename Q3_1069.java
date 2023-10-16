//Name: Uddalak Mukhopadhyay
//Registration Number: 2341013420
//Problem link: https://cses.fi/problemset/task/1069


import java.util.*;
public class Q3_1069 {
 
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String st=sc.next();
        System.out.println(maxcount(st));
        sc.close();
    }
 
    public static int maxcount(String str){
        int max=1;
        int i=0;
        int count=1;
        while(i<str.length()-1){
            if(str.charAt(i)==str.charAt(i+1)){
                count++;
                i++;
            }
            else{
                count=1;
                i++;
            }
            if(count>max){
                max=count;
            }
 
        }
        return max;
    }
}
