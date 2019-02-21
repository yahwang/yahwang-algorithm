import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        int e, s, m, res, cnt=0;
        Scanner sc = new Scanner(System.in);
        e = sc.nextInt();
        s = sc.nextInt();
        m = sc.nextInt();
        sc.close();
        while(true){
            res = 28*cnt+s;
            if((res-e)%15 == 0 && (res-m)%19 == 0){
                break;
            }
            cnt++;
        }
        System.out.println(res);
    }
}