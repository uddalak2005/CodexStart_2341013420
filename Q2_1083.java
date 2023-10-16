//Name: Uddalak Mukhopadhyay
//Registration Number: 2341013420
//Problem link: https://cses.fi/problemset/task/1083



import java.util.*;
public class Q2_1083 {
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt()-1;
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println(missingNumber(arr));
        sc.close();

    }

    public static int missingNumber(int[] arr){
        int i=0;
        while(i<arr.length){
            int correct=arr[i]-1;
            if(arr[i]<arr.length && arr[i]!=arr[correct]){
                swap(arr,i,correct);
            }
            else{
                i++;
            }
        }
        for(i=0;i<arr.length;i++){
            if(arr[i]!=i+1){
                return i+1;
            }
        }
        return arr.length+1;
    }

    public static void swap(int[] arr,int i, int correct){
        int temp=arr[i];
        arr[i]=arr[correct];
        arr[correct]=temp;
    }
}
