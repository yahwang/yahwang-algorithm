import java.io.*;

public class Quiz2579 {
    
    public static int[] dp;
    public static void main(String[] args) throws IOException{
        int size;
        int[] arr;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        size = Integer.parseInt(br.readLine());
        arr = new int[size+1];
        dp = new int[size+1];

        for(int i=1;i<=size;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp[0]=arr[0]=0;
        dp[1]=arr[1];
        if(size>=2){
            dp[2]=arr[1]+arr[2];
        }
        
        for(int i=3;i<=size;i++){
            dp[i] = Math.max(dp[i-3]+arr[i-1], dp[i-2])+arr[i];
        }
        
        System.out.println(dp[size]);
    }
}