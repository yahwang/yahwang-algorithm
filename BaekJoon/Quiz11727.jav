import java.io.*;

public class Quiz11727 {
    public static int[] res;
    public static void main(String[] args) throws IOException{
        int input;
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        input = Integer.parseInt(bf.readLine());
        res = new int[input+1];
        res[0]=0;
        for(int i=1;i<=input;i++){
            if(i==1){
                res[i] = 1;
            }
            else if(i==2){
                res[i] = 3;
            }
            else{
                res[i] = (res[i-1]+2*res[i-2])%10007;
            }
        }
        System.out.println(res[input]);
    }
}