// 참고 : https://jaemin8852.tistory.com/192

import java.io.*;
import java.util.StringTokenizer;

public class Quiz9465 {
    
    public static long[][] res;
    public static long[][] arr;
    public static void main(String[] args) throws IOException{
        int cnt, input;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        cnt = Integer.parseInt(br.readLine());
        while(cnt>0){
            input = Integer.parseInt(br.readLine());
            arr = new long[2][input+1];
            arr[0][0] = 0;
            arr[1][0] = 0;

            for(int i=0;i<=1;i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j=1;j<=input;j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            res = new long[2][input+1];
            res[0][0] = arr[0][0];
            res[1][0] = arr[1][0];
            
            res[0][1] = arr[0][1];
            res[1][1] = arr[1][1];

            for(int i=2;i<=input;i++){
                res[0][i]=Math.max(res[1][i-1],res[1][i-2])+arr[0][i];
                res[1][i]=Math.max(res[0][i-1],res[0][i-2])+arr[1][i];    
            }

            System.out.println(Math.max(res[0][input],res[1][input]));
            cnt--;
        }
    }
}