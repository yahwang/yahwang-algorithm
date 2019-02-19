import java.util.Arrays;
import java.util.Scanner;

public class Quiz2309{
    public static void main(String[] args){
        int[] height = new int[9];
        int totalSum=0;
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<9;i++){
            height[i] = sc.nextInt();
        }
        // 미리 정렬
        Arrays.sort(height);
        // 2개를 제외하는 조합 9C2 각 경우를 for문으로 구현
        for(int i=0;i<height.length-1;i++){
            for(int j=i+1;j<height.length;j++){
                // 해당 2개를 제외한 나머지의 합 계산
                for(int k=0;k<height.length;k++){
                    if(k!=i && k!= j){
                        totalSum+=height[k];
                    }
                }
                // 합이 100이면 출력 아니면 새 조합
                if(totalSum==100){
                    for(int l=0;l<height.length;l++){
                        if(l!=i && l!= j){
                            System.out.println(height[l]);
                        }    
                    }
                }
                else{
                    totalSum=0;
                    continue;
                }
            }
        }
    }
}