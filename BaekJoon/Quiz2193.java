import java.io.*;

public class Quiz2193 {
    
    public static long[][] res;
    public static void main(String[] args) throws IOException{
        int input;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = Integer.parseInt(br.readLine());
        res = new long[input+1][2];
        res[1][0]=0;
        res[1][1]=1;

        for(int i=2;i<=input;i++){
            if(res[i-1][1]>0){
                res[i][0] = res[i-1][1];
            }

            if(res[i-1][0]>0){
                res[i][0]+=res[i-1][0];
                res[i][1] = res[i-1][0];
            }   
        }
        System.out.println(res[input][0]+res[input][1]);
    }
}