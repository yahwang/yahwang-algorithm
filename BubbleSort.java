// 백준알고리즘 1427번
// https://www.acmicpc.net/problem/1427
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        String input;
        int temp;

        Scanner sc = new Scanner(System.in);
        input = sc.next();
        sc.close();
        int[] nums = new int[input.length()];
        for(int i=0;i<input.length();i++){
            nums[i] = Integer.parseInt(input.charAt(i)+"");
        }
        // 버블 정렬 알고리즘
        for(int i=0;i<nums.length-1;i++){
            for(int j=0;j<nums.length-1-i;j++){
                if(nums[j] > nums[j+1]){
                    temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        // 결과 출력
        for(int k=nums.length-1;k>-1;k--){
            System.out.print(nums[k]);
        }
    }
}