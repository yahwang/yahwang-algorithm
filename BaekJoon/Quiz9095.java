import java.util.Scanner;
import java.util.ArrayList;

public class Quiz9095{
    public static void main(String[] args){
        int input, cnt;
        Scanner sc = new Scanner(System.in);
        input = sc.nextInt();
        for(int i=0;i<input;i++){
            cnt=0;
            cnt = inorder(sc.nextInt(), cnt);
            System.out.println(cnt);
        }
    }
// DFS를 활용한 풀이
// 가능한 node의 value는 1,2,3
// 다음 node가 존재가능한 지 확인
// leaf node이면 count 증가
    public static int inorder(int num, int cnt){
        for(int i=1;i<=3;i++){
            if(num-i > 0){
                cnt = inorder(num-i, cnt);
            }
            else{
                cnt+=1;
                break;
            }
        }
        return cnt;
    }
}