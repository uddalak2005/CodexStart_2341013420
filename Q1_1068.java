//Name: Uddalak Mukhopadhyay
//Registration Number: 2341013420
//Problem link: https://cses.fi/problemset/task/1068



import java.util.*;
public class Q1_1068 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        long n=sc.nextLong();
        System.out.print(n+" ");
        weirdAlgorithm(n);
        sc.close();
    }
    public static void weirdAlgorithm(long n){
        if(n<=1){
            return;
        }
        
        if(n%2==0){
            n=n/2;
            System.out.print(n+" ");
            weirdAlgorithm(n);
        }
        else{
            n=(n*3)+1;
            System.out.print(n+" ");
            weirdAlgorithm(n);
        }
    }
    
}
