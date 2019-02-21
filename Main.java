import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        int e, s, m, res, cnt=0;
        Scanner sc = new Scanner(System.in);
        e = sc.nextInt();
        s = sc.nextInt();
        m = sc.nextInt();
        sc.close();

        // s로 만든 결과값을 e, m으로 각각 뺀 다음 나누어 떨어지는 지 확인
        // e.g.) 7 15 13 => 28*4+15 
        // ((28*4+15)-7) / 15 == 0
        // ((28*4+15)-13) / 19 == 0 
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